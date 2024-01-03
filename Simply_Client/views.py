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
    active_link = 'upload'
    return render(request, 'upload.html', {'active_link': active_link})


def tracking(request):
    return render(request, 'tracking.html')


def trackingDone(request):
    return render(request, 'tracking2.html')


def qris(request):
    return render(request, 'qris.html')


def formRegis(request):
    active_link = 'registration'
    return render(request, 'form-reg.html', {'active_link': active_link})


def payment(request):
    return render(request, 'payment-opt.html')
