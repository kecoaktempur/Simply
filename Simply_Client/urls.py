from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('qris', views.qris, name='qris'),
    path('upload', views.upload, name='upload'),
    path('tracking', views.tracking, name='tracking'),
    path('tracking-done', views.trackingDone, name='tracking2'),
    path('registration', views.formRegis, name='regis'),
    path('payment', views.payment, name='payment')
]
