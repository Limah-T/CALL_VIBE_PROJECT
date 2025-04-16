from django.contrib import admin
from accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "country", "phonenumber", "gender", "date_joined", "last_login"]
    list_filter = ["date_joined", "email"]
    search_fields = ["first_name", "last_name", "email", "country", "phonenumber"]

