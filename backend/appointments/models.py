# appointments/models.py
# Modelo para gestionar las citas del sistema GHL Sala 02
from django.db import models

class Contact(models.Model):
    """Modelo para gestionar contactos de GHL"""
    ghl_id = models.CharField(max_length=100, unique=True)
    location_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.ghl_id})"

class Appointment(models.Model):
    ghl_id = models.CharField(max_length=100, unique=True)
    location_id = models.CharField(max_length=100)
    calendar_id = models.CharField(max_length=100)
    contact_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default="Cita")
    appointment_status = models.CharField(max_length=50, default="confirmed")
    assigned_user_id = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    source = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.ghl_id})"
