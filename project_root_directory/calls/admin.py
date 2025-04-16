from django.contrib import admin
from calls.models import Call

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'to_number', 'from_number', 'duration', 'call_time', 'status']
    list_filter = ['status']
    search_fields = ['call_time']