from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('qris', views.qris, name='qris'),
    path('upload', views.upload, name='upload')
]
