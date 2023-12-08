from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('tracking', views.tracking, name='tracking'),
    path('tracking-done', views.trackingDone, name='tracking2'),
]
