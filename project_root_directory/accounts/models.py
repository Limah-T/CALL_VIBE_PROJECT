from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

GENDER = [
    ('male', 'Male'),
    ('female', 'Female')
]

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, country, phonenumber, password=None, **extra_fields):
        if not first_name:
            raise ValueError("First name must be set!")
        if not last_name:
            raise ValueError("Last name must be set!")
        if not email:
            raise ValueError("email must be set!")
        if not username:
            raise ValueError("Username must be set!")
        if not country:
            raise ValueError("Country must be set!")
        if not phonenumber:
            raise ValueError("Phone number must be set!")
        email = self.normalize_email(email=email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, username=username, country=country, phonenumber=phonenumber, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, country, phonenumber, password=None,  **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must be set to True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must be set to True")
        return self.create_user(first_name, last_name, email, username, country, phonenumber, password, **extra_fields)

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(unique=True, max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    phonenumber = models.CharField(max_length=15, unique=True, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "country", "phonenumber"]
    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()
