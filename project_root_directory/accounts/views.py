from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from .forms import RegistrationForm, LoginForm
from .models import CustomUser
from .verify_phonenumber import SendSMS
import jwt
import os
import rest_framework

from .mail_box import send_welcome_message, send_verification_message

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')

temporary_storage = {
    'first_name': '', 'last_name': '', 'email':'', 'username': '', 'country': '', 'phonenumber': '', 'gender': '', 'password': ''
}

# Register user and process verification of credentials
class RegistrationView(FormView):
    global temporary_storage
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:profile")

    def post(self, request, *args, **kwargs):
        
        form = self.get_form(self.form_class)
        if form.is_valid():
            temporary_storage['first_name'] = form.cleaned_data['first_name']
            temporary_storage['last_name'] = form.cleaned_data['last_  hhname']
            temporary_storage['email'] = form.cleaned_data['email']
            temporary_storage['username'] = form.cleaned_data['username']
            temporary_storage['country'] = form.cleaned_data['country']
            phonenumber = form.cleaned_data['phonenumber']
            temporary_storage['gender'] = form.cleaned_data['gender']
            temporary_storage['password'] = form.cleaned_data['password']
            # Create an instance and call send
            sending = SendSMS()
            sending.send()            
            return redirect(reverse_lazy("accounts:generate_token_for_email", kwargs={'email': temporary_storage['email'], 'username':  temporary_storage['username']}))
        return super().post(request, *args, **kwargs)

# Login in verify users   
class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts:profile")

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user:
                print(True)
            print(False)
            print(user)
            return HttpResponse("form submitted")        
        return super().post(request, *args, **kwargs)

# Set expiration set for JWT token
def get_token_expiration(hours=0, minutes=0, seconds=0):
    # 15 minutes from now on
    expiry = datetime.now(timezone.utc) + timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return expiry

# Generate the JWT token
def generate_token_for_email(request, email, username):
    expiration = get_token_expiration(hours=0, minutes=15, seconds=0)
    # Current time (UTC, timezone-aware)
    now = datetime.now(timezone.utc)
    # Convert to UNIX Timestamps
    iat = int(now.timestamp())
    expiration_time = int(expiration.timestamp())
    payload = {
        'email': email,
        'exp': expiration_time, # expires in 15 mins
        'iat': iat,  # issued at
    }
    token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    # call the verification_link function
    verification_link = f"http://127.0.0.1:8000/accounts/verify-email?token={token}"
    send_verification_message(sender_email=os.getenv('EMAIL_HOST_USER'), recipient_email=email, recipient_name=username, token=verification_link)
    return render(request, "accounts/email_alert.html", {'email': email, 'username': username}) 

# Verify incoming JWT token with the provided token
def verify_email(request):
    global temporary_storage
    token = request.GET.get('token')
    try:
        pay_load = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print("Token is valid", pay_load)
        print(temporary_storage)
        return redirect(reverse_lazy("home:home"))
    except jwt.ExpiredSignatureError:
        return render(request, "accounts/failed_verification.html")
    except jwt.InvalidTokenError:
        return HttpResponse("Invalid Verification Token")
    
# Failed Verification View
def resend_verification(request):
    return HttpResponse("In failed view")


# # Save user's credentials and login them in  
# def verify_phone_number():
#     phonenumber = user_temporary_phone_num_storage['phonenumber']

    ...
    # first_name = form.cleaned_data['first_name']
    # last_name = form.cleaned_data['last_name']
    # email = form.cleaned_data['email']
    # username = form.cleaned_data['username']
    # country = form.cleaned_data['country']
    # phonenumber = form.cleaned_data['phonenumber']
    # gender = form.cleaned_data['gender']
    # password = form.cleaned_data['password']
    # print(email, username)

# Authenticated user's profile view
class ProfileView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy("accounts:register")
    template_name = "accounts/profile.html"
    queryset = CustomUser.objects.all()
    context_object_name = "user"
    lookup_field = "pk"

# Logout user and redirect to home
@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("home:home"))