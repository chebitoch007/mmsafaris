# ============================================
# core/models.py
# ============================================
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class Tour(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    duration_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    max_group_size = models.PositiveIntegerField(default=12)
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-featured', '-created_at']

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_people = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    preferred_date = models.DateField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.tour.name}"

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