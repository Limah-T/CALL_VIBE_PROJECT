from django import forms
from .models import CustomUser, GENDER
COUNTRY = [
    ("Algeria", "Algeria"),
    ("Angola", "Angola"),
    ("Egypt", "Egypt"),
    ("Ethopia", "Ethiopia"),
    ("Ghana", "Ghana"),
    ("Kenya", "Kenya"),
    ("Libya", "Libya"),
    ("Nigeria", "Nigeria"),
    ("South africa", "South Africa"),
    ("Uganda", "Uganda")
]

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100, required=True)
    country = forms.ChoiceField(choices=COUNTRY, required=True)
    phonenumber = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'country', 'phonenumber', 'gender']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        # Apply the form-control class to each form field
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)