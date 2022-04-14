from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dentist_3_project.accounts.models import Profile
from dentist_3_project.core.models import Appointment, Review
from dentist_3_project.services.models import Service

UserModel = get_user_model()

class TestAddReview(TestCase):

    def __create_service(self):
        service = Service.objects.create(treatment='Teeth Whitening',
                                         category='1',
                                         duration='60',
                                         price='50')
        service.full_clean()
        service.save()
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
        appointment.full_clean()
        appointment.save()
        return appointment


    def __create_profile(self, user):
        profile = Profile.objects.create(first_name='evge',
                                         last_name='kosta',
                                         dob='1988-12-12',
                                         gender='male',
                                         phone='12325345',
                                         user=user
                                         )
        profile.full_clean()
        profile.save()
        return profile

    def __create_review(self, appointment, user):
        review = Review.objects.create(title='Happy',
                                       body='I am quite satisfied with the Docs skills',
                                       user=user,
                                       appointment=appointment)
        return review



    def test_build_add_review__creates_review_in_db__expect_success(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        appointment = self.__create_appointment(service, user)
        review_data = {'title': 'Happy',
                       'body': 'I am quite satisfied with the Docs skills',
                       'user': user,
                       'appointment': appointment}

        response = self.client.post(path=reverse('show add review', kwargs={'pk': appointment.id}), data=review_data)
        review = Review.objects.first()
        self.assertIsNotNone(review)

    def test_edit_review__edits_review_successfully(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        appointment = self.__create_appointment(service, user)
        review = self.__create_review(appointment, user)
        review_data = {'title': 'edited_review',
                       'body': 'this is the edited veersion',
                       'user': user,
                       'appointment': appointment}

        response = self.client.post(path=reverse('show edit review', kwargs={'pk': review.id}), data=review_data)
        edited_review = Review.objects.first()
        self.assertNotEqual(review.title, edited_review.title)

    # this one returns status code 200 , but it does not delete in database. why?
    def test_delete_review__deletes_review_successfully(self):
        service = self.__create_service()
        user = UserModel.objects.create_user(email='testuser@mail.com', password='7890plioK')
        logged_in = self.client.login(email='testuser@mail.com', password='7890plioK')
        appointment = self.__create_appointment(service, user)
        review = self.__create_review(appointment, user)

        response = self.client.delete(reverse('show delete review', kwargs={'pk': review.id}))
        review = Review.objects.first()
        print(review, response.status_code)
        self.assertIsNone(review)