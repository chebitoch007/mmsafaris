# ============================================
# core/admin.py
# ============================================
from django.contrib import admin
from .models import Tour, Booking, ContactMessage

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price', 'difficulty', 'featured']
    list_filter = ['difficulty', 'featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'tour', 'preferred_date', 'number_of_people', 'created_at']
    list_filter = ['tour', 'preferred_date']
    search_fields = ['full_name', 'email']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
