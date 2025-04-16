from . import views
from django.urls import path

urlpatterns = [
    path('https://napukfok.developers.africastalking.com/incoming-messages', views.incoming_messages),
]