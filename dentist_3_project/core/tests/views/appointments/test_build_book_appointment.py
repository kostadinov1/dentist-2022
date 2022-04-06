from django.contrib.auth import get_user_model
from django.test import TestCase

from dentist_3_project.core.models import Appointment
from dentist_3_project.services.models import Service

UserModel = get_user_model()

class TestBuildAppointment(TestCase):
    pass
    VALID_USER_DATA = {
        'email': 'evga@mail.com',
        'password': '7890plioK'
    }
    VALID_PROFILE_DATA = {
        'name': 'Evga',
        'phone': '0987787234'
    }
    VALID_SERVICE_DATA = {
        'treatment': 'Teeth Whitening',
        'category': 'Preventative',
        'duration': '60',
        'price': '50'
    }

    VALID_APPOINTMENT_DATA = {
        'venue': 'Balchik',
        'date': '2022-01-11',
        'time': '14:00:00',
        'message': 'I want to book appointment please doc!!',

    }

    def test_appointment_create_in_database(self):
        user = UserModel.objects.create(email='evga@mail.com',
                                        password='7890plioK')

        service = Service.objects.create(treatment='Teeth Whitening',
                                         category='Preventative',
                                         duration='60',
                                         price='50')

        appointment = Appointment.objects.create(
            venue=self.VALID_APPOINTMENT_DATA['venue'],
            date=self.VALID_APPOINTMENT_DATA['date'],
            time=self.VALID_APPOINTMENT_DATA['time'],
            message=self.VALID_APPOINTMENT_DATA['message'],
            user=user,
            service=service

        )
        appointment.full_clean()
        appointment.save()
        self.assertIsNotNone(Appointment.objects.all()[0])

    def test_appointment_deletes_in_database(self):
        user = UserModel.objects.create(email='evga@mail.com',
                                        password='7890plioK')

        service = Service.objects.create(treatment='Teeth Whitening',
                                         category='Preventative',
                                         duration='60',
                                         price='50')

        appointment = Appointment.objects.create(
            venue=self.VALID_APPOINTMENT_DATA['venue'],
            date=self.VALID_APPOINTMENT_DATA['date'],
            time=self.VALID_APPOINTMENT_DATA['time'],
            message=self.VALID_APPOINTMENT_DATA['message'],
            user=user,
            service=service

        )
        appointment.full_clean()
        appointment.save()
        appointment.delete()
        self.assertEqual(Appointment.objects.all().count(), 0)

    def test_book_appointment__send_email_successful(self):
        pass

    def test_book_appointment__send_email_raises_error_on_fail(self):
        pass