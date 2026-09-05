from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Service, Booking
from .forms import BookingForm, RegistrationForm


def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')

        user = None
        if email and password:
            account = User.objects.filter(email__iexact=email).first()
            if account:
                user = authenticate(
                    request,
                    username=account.username,
                    password=password
                )

        if user is not None:
            login(request, user)
            if Booking.objects.filter(booked_by=user).exists():
                return redirect('my_bookings')

            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid email or password',
                'next': request.POST.get('next') or request.GET.get('next', ''),
            })

    return render(request, 'login.html', {
        'next': request.GET.get('next', ''),
    })


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.POST.get('next', '')
            login_url = redirect('login').url
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(f'{login_url}?next={next_url}')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registation.html', {
        'form': form,
        'next': request.POST.get('next') or request.GET.get('next', ''),
    })

#------------ Login after  Booking  Request ------------#

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')

# ------ Tracker view for my bookings ------#

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(booked_by=request.user).order_by('-date', '-time')

    if not bookings.exists():
        return redirect('home')

    return render(request, 'tracker.html', {
        'bookings': bookings
    })