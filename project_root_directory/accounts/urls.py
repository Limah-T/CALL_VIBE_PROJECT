from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('generate_token/<str:email>/<str:username>/', views.generate_token_for_email, name="generate_token_for_email"),
    path('verify-email/', views.verify_email, name="verify-email"),
    path('resend_verification', views.resend_verification, name='resend_verification'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout_user/', views.logout_user, name='logout'),
]