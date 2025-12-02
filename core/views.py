# ============================================
# core/views.py
# ============================================
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tour, Booking, ContactMessage
from .forms import BookingForm, ContactForm

def home(request):
    featured_tours = Tour.objects.filter(featured=True)[:3]
    context = {'featured_tours': featured_tours}
    return render(request, 'core/home.html', context)

def tours(request):
    tours_list = Tour.objects.all()
    context = {'tours': tours_list}
    return render(request, 'core/tours.html', context)

def tour_detail(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    context = {'tour': tour}
    return render(request, 'core/tour_detail.html', context)

def booking(request, slug):
    tour = get_object_or_404(Tour, slug=slug)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.save()
            messages.success(request, 'Your booking request has been submitted! We will contact you soon.')
            return redirect('tour_detail', slug=tour.slug)
    else:
        form = BookingForm()

    context = {'form': form, 'tour': tour}
    return render(request, 'core/booking.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'core/contact.html', context)