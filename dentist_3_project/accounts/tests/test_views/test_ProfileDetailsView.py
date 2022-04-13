import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dentist_3_project.accounts.models import Profile
from dentist_3_project.core.models import Appointment, Review
from dentist_3_project.services.models import Service

UserModel = get_user_model()

class TestProfileDetailsView(TestCase):

    IMAGE = tempfile.NamedTemporaryFile(suffix=".jpg").name

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
                                         image= self.IMAGE,
                                         user=user
                                         )
        return profile

    def __create_review(self, appointment, user):
        review = Review.objects.create(title='Happy',
                                       body='I am quite satisfied with the Docs skills',
                                       user=user,
                                       appointment=appointment)
        return review

    def test__open_non_existing_profile_expect_404(self):
        response = self.client.get(reverse('show profile view', kwargs={'pk': 1}))

        self.assertEqual(404, response.status_code)

    def test_get__expect_correct_template(self):
        user = UserModel.objects.create(email='evgani@mail.com', password='7890plioK')
        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))
        self.assertTemplateUsed('auth/profile-view.html')

    def test_profile_view_show_own_appointments(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        self.client.login(email='testuser@mail.com', password='7890plioK')

        appointment = self.__create_appointment(service, user)
        profile = self.__create_profile(user)

        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))
        self.assertIsNotNone(response.context['appointments'])

    def test_profile_view_show_no_appointments(self):
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        self.client.login(email='testuser@mail.com', password='7890plioK')

        profile = self.__create_profile(user)

        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))
        self.assertEqual(len(response.context['appointments']), 0)

    def test_profile_view_show_own_reviews(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        self.client.login(email='testuser@mail.com', password='7890plioK')

        appointment = self.__create_appointment(service, user)
        profile = self.__create_profile(user)


        appointment.full_clean()
        appointment.save()
        review = self.__create_review(appointment, user)

        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))
        self.assertIsNotNone(response.context['reviews'])

    def test_profile_view_show_no_reviews(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        self.client.login(email='testuser@mail.com', password='7890plioK')

        appointment = self.__create_appointment(service, user)
        profile = self.__create_profile(user)

        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))
        self.assertIsNotNone(len(response.context['reviews']), 0)



