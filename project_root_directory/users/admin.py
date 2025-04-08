from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "country", "phonenumber", "date_joined", "last_login"]
    list_filter = ["date_joined", "email"]
    search_fields = ["first_name", "last_name", "email", "country", "phonenumber"]

