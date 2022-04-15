from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dentist_3_project.accounts.models import Profile
from dentist_3_project.core.forms import AppointmentForm
from dentist_3_project.core.models import Appointment
from dentist_3_project.services.models import Service

UserModel = get_user_model()

class TestBuildAppointment(TestCase):


    def __create_service(self):
        service = Service.objects.create(treatment='Teeth Whitening',
                                         category='Preventative',
                                         duration='60',
                                         price='50')
        service.full_clean()
        service.save()
        return service

    def __create_appointment(self, service, user):
        appointment = Appointment.objects.create(
            venue='Varna',
            time='14:00',
            date='2022-12-12',
            message='I want an appointment please',
            user=user,
            service=service
        )
        appointment.full_clean()
        appointment.save()
        return appointment

    def __create_profile(self, user):
        profile = Profile.objects.create(first_name='evge',
                                         last_name='kosta',
                                         dob='1988-12-12',
                                         gender='Male',
                                         phone='12325345',
                                         user=user
                                         )
        profile.full_clean()
        profile.save()
        return profile


    def test_appointment_create_is_successful(self):
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        service = self.__create_service()
        profile = self.__create_profile(user)

        appointment_data = {'venue': 'Varna',
                            'time': '14:00',
                            'date': '2022-12-12',
                            'message': 'I want an appointment please',
                            'user': user,
                            'service': service
                            }
        response = self.client.post(reverse('show book appointment'), data=appointment_data)

        appointment = Appointment.objects.get()
        print(appointment, response.status_code)
        self.assertIsNotNone(appointment)

    # NOT WORKING PROPERLY
    def test_appointment_deletes_in_database(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        profile = self.__create_profile(user)
        appointment = self.__create_appointment(service, user)
        response = self.client.post(reverse('show delete appointment', kwargs={'pk': appointment.id}))
        check = Appointment.objects.all()
        print(appointment, response.status_code, response)
        self.assertEqual(len(check), 0)


    def test_book_appointment__send_email_successful(self):
        pass

    def test_book_appointment__send_email_raises_error_on_fail(self):
        pass