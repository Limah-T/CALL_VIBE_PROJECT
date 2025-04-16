from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'contact_name', 'contact_number']
    list_filter = ['user_id']
    search_fields = ['contact_name', 'contact_number']