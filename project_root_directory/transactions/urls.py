from django.urls import path
from . import views

app_name = "transactions"

urlpatterns = [
    path('purchase-airtime/', views.purchase_airtime, name="purchase-airtime"),
]