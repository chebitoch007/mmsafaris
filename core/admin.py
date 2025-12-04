# ============================================
# core/admin.py
# ============================================
from django.contrib import admin
from .models import Tour, Booking, ContactMessage, TourImage, ItineraryDay

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1

class ItineraryDayInline(admin.StackedInline):
    model = ItineraryDay
    extra = 1

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price', 'difficulty', 'featured']
    list_filter = ['difficulty', 'featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TourImageInline, ItineraryDayInline]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'tour', 'preferred_date', 'number_of_people', 'status', 'created_at']
    list_filter = ['status', 'tour', 'preferred_date']
    search_fields = ['full_name', 'email']
    list_editable = ['status']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']