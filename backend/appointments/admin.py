from django.contrib import admin
from .models import Appointment, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('ghl_id', 'first_name', 'last_name', 'email', 'phone', 'source', 'date_added')
    list_filter = ('source', 'date_added', 'location_id')
    search_fields = ('ghl_id', 'first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('ghl_id', 'date_added', 'date_updated')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('ghl_id', 'title', 'contact_id', 'appointment_status', 'start_time', 'end_time')
    list_filter = ('appointment_status', 'start_time', 'location_id')
    search_fields = ('ghl_id', 'title', 'contact_id', 'notes')
    readonly_fields = ('ghl_id', 'date_added', 'date_updated')
