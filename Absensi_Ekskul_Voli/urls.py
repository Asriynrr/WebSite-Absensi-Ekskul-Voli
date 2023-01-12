from django.contrib import admin
from django.urls import path
from Absensi_Ekskul_Voli.views import absen

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('absen/', absen),  
]
