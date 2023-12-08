from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')

def qris(request):
    return render(request, 'qris.html')

def upload(request):
    return render(request, 'upload.html')