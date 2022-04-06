from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from dentist_3_project.accounts.models import Profile

UserModel = get_user_model()


class TestProfileModel(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Gosho',
        'last_name': 'Tarikatkov',
        'dob': '1987-12-12',
        'gender': 'Male',
        'phone': '087879898',
        }

    def test_profile__first_name_only_letter__expect_success(self):
        user = UserModel.objects.create(email='evgeni13@mail.com', password='7890plioK')
        profile = Profile(**self.VALID_PROFILE_DATA, user=user)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile__first_name_contain_digit__expect_fail(self):
        user = UserModel.objects.create(email='evgeni13@mail.com', password='7890plioK')
        profile = Profile(
                          first_name='Gosh1',
                          last_name='Tarikatkov',
                          phone='087879898',
                          user=user
                          )

        with self.assertRaises(ValidationError) as err:
            # DO NOT FORGET THE FULL CLEAN WHEN TESTING MODELS
            # FORMS DO IT IMPLICITLY
            # HERE IT MUST BE CALLED EXPLICITLY
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(err.exception)

    def test_profile__first_name_contain_white_space__expect_fail(self):
        user = UserModel.objects.create(email='evgeni13@mail.com', password='7890plioK')
        profile = Profile(
            first_name='Go sh',
            last_name='Tarikatkov',
            dob='1987-12-12',
            gender='Male',
            phone='087879898',
            user=user
        )
        with self.assertRaises(ValidationError) as err:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(err.exception)

    def test_profile__first_name_contain_a_dot_expect_fail(self):
        user = UserModel.objects.create(email='evgeni13@mail.com', password='7890plioK')
        profile = Profile(
            first_name='Gos.h',
            last_name='Tarikatkov',
            dob='1987-12-12',
            gender='Male',
            phone='087879898',
            user=user
        )
        with self.assertRaises(ValidationError) as err:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(err.exception)

    def test_profile__full_name_returns_full_name_expect_success(self):
            user = UserModel.objects.create(email='evgeni13@mail.com', password='7890plioK')
            profile = Profile(
                first_name='Gosho',
                last_name='Tarikatkov',
                dob='1987-12-12',
                gender='Male',
                phone='087879898',
                user=user
            )
            profile.save()

            self.assertEqual('Gosho Tarikatkov', profile.__str__())
