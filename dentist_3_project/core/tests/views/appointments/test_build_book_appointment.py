from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dentist_3_project.accounts.models import Profile
from dentist_3_project.core.models import Appointment
from dentist_3_project.services.models import Service

UserModel = get_user_model()

class TestBuildAppointment(TestCase):


    def __create_service(self):
        service = Service.objects.create(treatment='Teeth Whitening',
                                         category='Preventative',
                                         duration='60',
                                         price='50')
        return service

    def __create_appointment(self, service, user):
        appointment = Appointment.objects.create(
            venue='Varna',
            date='2022-12-12',
            time='14:00',
            message='I want an appointment please',
            user=user,
            service=service
        )
        return appointment

    def __create_profile(self, user):
        profile = Profile.objects.create(first_name='evge',
                                         last_name='kosta',
                                         dob='1988-12-12',
                                         gender='male',
                                         phone='12325345',
                                         user=user
                                         )
        return profile


    def test_appointment_create_in_successful(self):
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        service = self.__create_service()
        profile = self.__create_profile(user)
        appointment_data = {'venue': 'Varna',
                        'date': '2022-12-12',
                        'time': '14:00',
                        'message': 'I want an appointment please',
                        'phone': '123543534',
                        'user': user,
                        'service': service
                        }
        response = self.client.post(path=reverse('show book appointment'), data=appointment_data)
        appointment = Appointment.objects.all()
        print(appointment, response.status_code)
        self.assertIsNotNone(appointment)


    def test_appointment_deletes_in_database(self):
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        self.client.login(email='testuser@mail.com', password='7890plioK')
        service = self.__create_service()
        appointment = self.__create_appointment(service, user)
        response = self.client.post(path=reverse('show delete appointment', kwargs={'pk': appointment.id}))
        appointment = Appointment.objects.first()
        print(appointment, response.status_code)
        self.assertIsNone(appointment)

    def test_book_appointment__send_email_successful(self):
        pass

    def test_book_appointment__send_email_raises_error_on_fail(self):
        pass