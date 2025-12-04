# ============================================
# core/views.py
# ============================================
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from .models import Tour, Booking, ContactMessage
from .forms import BookingForm, ContactForm


def home(request):
    featured_tours = Tour.objects.filter(featured=True)[:3]
    context = {'featured_tours': featured_tours}
    return render(request, 'core/home.html', context)


def tours(request):
    # Start with all tours
    tours_list = Tour.objects.all()

    # 1. Search (Name or Description)
    query = request.GET.get('q')
    if query:
        tours_list = tours_list.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # 2. Filter by Difficulty
    difficulty = request.GET.get('difficulty')
    if difficulty:
        tours_list = tours_list.filter(difficulty=difficulty)

    # 3. Filter by Price (Max Price)
    max_price = request.GET.get('max_price')
    if max_price:
        try:
            tours_list = tours_list.filter(price__lte=max_price)
        except ValueError:
            pass  # Ignore invalid price inputs

    context = {
        'tours': tours_list,
        # Pass current filters back to template to keep fields populated
        'current_difficulty': difficulty,
        'current_price': max_price,
        'current_query': query
    }
    return render(request, 'core/tours.html', context)


def tour_detail(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    # The template can now access tour.gallery_images.all and tour.itinerary.all
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

            # --- Email Notification Logic ---
            # 1. Send Receipt to Customer
            subject_user = f"Booking Received: {tour.name}"
            message_user = f"Hi {booking.full_name},\n\nWe have received your booking request for {tour.name} on {booking.preferred_date}.\n\nWe will review availability and get back to you shortly with a quote and payment details.\n\nBest,\nM&M Africa Safaris"

            send_mail(
                subject_user,
                message_user,
                settings.DEFAULT_FROM_EMAIL,
                [booking.email],
                fail_silently=True,
            )

            # 2. Notify Admin
            subject_admin = f"New Booking Request: {booking.full_name}"
            message_admin = f"New booking for {tour.name}.\nDate: {booking.preferred_date}\nPax: {booking.number_of_people}\nEmail: {booking.email}\nPhone: {booking.phone}"

            # Assuming you have an ADMINS list or a specific receiver email
            admin_email = getattr(settings, 'ADMIN_EMAIL', 'info@mmsafaris.com')

            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
                fail_silently=True,
            )
            # --------------------------------

            messages.success(request, 'Your booking request has been submitted! Check your email for confirmation.')
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
            contact_msg = form.save()

            # Notify Admin
            subject = f"New Contact Message from {contact_msg.name}"
            message = f"Subject: {contact_msg.subject}\n\nMessage:\n{contact_msg.message}\n\nFrom: {contact_msg.email}"
            admin_email = getattr(settings, 'ADMIN_EMAIL', 'info@mmsafaris.com')

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
                fail_silently=True,
            )

            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'core/contact.html', context)