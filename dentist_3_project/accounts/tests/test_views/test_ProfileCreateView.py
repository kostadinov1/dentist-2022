from django.contrib.auth import get_user_model
from django.test import TestCase , Client
from django.urls import reverse
import tempfile

from dentist_3_project.accounts.models import Profile

UserModel = get_user_model()

class ProfileCreateViewTests(TestCase):

    IMAGE = tempfile.NamedTemporaryFile(suffix=".jpg").name

    def __create_profile(self, user):
        profile = Profile.objects.create(first_name='evge',
                                         last_name='kosta',
                                         dob='1988-12-12',
                                         gender='male',
                                         phone='12325345',
                                         image= self.IMAGE,
                                         user=user
                                         )
        profile.full_clean()
        profile.save()
        return profile


    def test_post_expect_correct_template_used(self):
        # user = UserModel.objects.create(email='evga@mail.com', password='7890plioK')
        user = UserModel.objects.create_user(email='evga@mail.com', password='7890plioK')
        # loged_in = self.client.login(email='evga@mail.com', password='7890plioK')
        response = self.client.post(reverse('show profile create'))

        self.assertTemplateUsed('auth/profile-create.html')



    def test_create_profile__when_valid_expect_success(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testov',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        self.client.post(reverse('show profile create'), data=profile_info)
        profile = Profile.objects.first()
        print(profile)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.first_name, 'evgeni')
        self.assertEqual(profile.last_name, 'testov')

    def test_create_profile__when_NOT_valid_expect_raises(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testo23v',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        self.client.post(reverse('show profile create'), data=profile_info)
        profile = Profile.objects.first()
        print(profile)

    def test_gets_correct_template_used(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testov',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        self.client.post(reverse('show profile create'), data=profile_info)
        self.assertTemplateUsed('auth/profile-create.html')

    def test_when_all_valid_correct_redirect(self):
        user = UserModel.objects.create_user(email='evga@mail.com',
                                        password='7890plioK')
        self.client.login(email='evga@mail.com', password='7890plioK')

        profile_info = {'first_name': 'evgeni',
                        'last_name': 'testov',
                         'dob': '1987-12-12',
                        'gender': 'Male',
                        'phone': '123543534',

                        'user': user
                        }
        response = self.client.post(reverse('show profile create'), data=profile_info)
        self.assertRedirects(response, '/')


    # test status code