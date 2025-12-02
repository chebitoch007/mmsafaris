# ============================================
# core/forms.py
# ============================================
from django import forms
from .models import Booking, ContactMessage

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'number_of_people', 'preferred_date', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1', 'min': '1'}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select Date'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Dietary restrictions, allergies, etc.'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Booking Inquiry'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'How can we help you plan your safari?'}),
        }