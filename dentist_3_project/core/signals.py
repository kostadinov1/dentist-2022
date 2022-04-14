from django.core.mail import send_mail
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

from dentist_3_project.core.models import Appointment

from django.apps import AppConfig


@receiver(post_save, sender=Appointment)
def send_appointment_email(instance, **kwargs):
    appointment = instance
    venue = appointment.cleaned_data['venue']
    date = appointment.cleaned_data['date']
    time = appointment.cleaned_data['time']
    message = appointment.cleaned_data['message']
    name = appointment.user.profile.first_name
    phone = appointment.user.profile.phone
    email = appointment.user.email
    send_mail(f'Appointment from {name} at {date}{time} at {venue} with phone number: {phone} and email: {email}',
              message, f'{email}', ['evgenikostadinov1987@gmail.com'])

#
# class MyAppConfig(AppConfig):
#     ...
#
#     def ready(self):
#         from . import signals
#         # Implicitly connect a signal handlers decorated with @receiver.
#         # Explicitly connect a signal handler.
#         request_finished.connect(signals.send_appointment_email)
#
