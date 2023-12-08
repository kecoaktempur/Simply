from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def tracking(request):
    return render(request, 'tracking.html')


def trackingDone(request):
    return render(request, 'tracking2.html')


def qris(request):
    return render(request, 'qris.html')


def upload(request):
    return render(request, 'upload.html')
