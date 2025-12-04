# ============================================
# core/models.py
# ============================================
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse

class Tour(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()  # Main overview
    duration_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    max_group_size = models.PositiveIntegerField(default=12)
    image = models.ImageField(upload_to='tours/', blank=True, null=True) # Main thumbnail
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tour_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-featured', '-created_at']

# New Model: Gallery Images
class TourImage(models.Model):
    tour = models.ForeignKey(Tour, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tours/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.tour.name}"

# New Model: Detailed Itinerary
class ItineraryDay(models.Model):
    tour = models.ForeignKey(Tour, related_name='itinerary', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)  # e.g., "Day 1: Arrival"
    description = models.TextField()
    accommodation = models.CharField(max_length=200, blank=True)
    meals = models.CharField(max_length=100, blank=True, help_text="e.g., B, L, D")

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number}: {self.tour.name}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Inquiry'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Fully Paid'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_people = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    preferred_date = models.DateField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.tour.name} ({self.get_status_display()})"

    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']