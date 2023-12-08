from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')

def formRegis(request):
    return render(request, 'form-reg.html')

def payment(request):
    return render(request, 'payment-opt.html')