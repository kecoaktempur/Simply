from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def formRegis(request):
    active_link = 'registration'
    done_state = False
    return render(request, 'form-reg.html', {'active_link': active_link, 'done_state': done_state})


def payment(request):
    active_link = 'payment'
    done_state = False
    return render(request, 'payment-opt.html', {'active_link': active_link, 'done_state': done_state})


def qris(request):
    active_link = 'payment'
    done_state = False
    return render(request, 'qris.html', {'active_link': active_link, 'done_state': done_state})


def upload(request):
    active_link = 'upload'
    done_state = False
    return render(request, 'upload.html', {'active_link': active_link, 'done_state': done_state})


def validation(request):
    active_link = 'validation'
    done_state = False
    return render(request, 'validation.html', {'active_link': active_link, 'done_state': done_state})


def schedule(request):
    active_link = 'schedule'
    done_state = False
    return render(request, 'schedule.html', {'active_link': active_link, 'done_state': done_state})


def tracking(request):
    active_link = 'tracking'
    done_state = False
    return render(request, 'tracking.html', {'active_link': active_link, 'done_state': done_state})


def trackingDone(request):
    return render(request, 'tracking2.html')
