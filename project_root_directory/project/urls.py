from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('accounts/', include('accounts.urls')),
    path('about/', include("about.urls")),
    path('transactions', include('transactions.urls')),
    path('api/', include('api.urls')),
]
