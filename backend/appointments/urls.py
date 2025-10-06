from django.urls import path
from . import views

urlpatterns = [
    # Contactos
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='contact-create'),
    
    # Citas
    path('appointments/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<str:appointment_id>/update/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointments/<str:appointment_id>/delete/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),
    
    # Webhook
    path('webhook/ghl/', views.ghl_webhook, name='ghl-webhook'),
]
