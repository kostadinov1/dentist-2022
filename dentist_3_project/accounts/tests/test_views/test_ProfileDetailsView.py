from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from dentist_3_project.accounts.models import Profile

UserModel = get_user_model()

class TestProfileDetailsView(TestCase):
    VALID_USER_DATA = {
        'email': 'evga@mail.com',
        'password': '7890plioK'
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Gosho',
        'last_name': 'Tarikatkov',
        'dob': '1987-12-12',
        'gender': 'Male',
        'phone': '087879898',
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

    def test__open_non_existing_profile_expect_404(self):
        response = self.client.get(reverse('show profile view', kwargs={'pk': 1}))

        self.assertEqual(404, response.status_code)


    def test_get__expect_correct_template(self):
        user = UserModel.objects.create(email='evgani@mail.com', password='7890plioK')
        #self.client.login()
        # profile = Profile.objects.create(first_name='Gosho',
        #                                 last_name='Tarikatkov',
        #                                 phone='087879898',
        #                                 )
        response = self.client.get(reverse('show profile view', kwargs={'pk': user.id}))

        self.assertTemplateUsed('auth/profile-view.html')




