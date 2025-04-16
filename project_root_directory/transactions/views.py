from django.shortcuts import render

def send_money(request):
    return render(request, "transactions/airtime_purchase.html")

