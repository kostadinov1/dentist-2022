from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from dentist_3_project.accounts.models import Profile, AppUser
from dentist_3_project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin

UserModel = get_user_model()
YEARS_CHOICES = range(1920, 2022)


class CreateProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'dob': forms.SelectDateWidget(
                years=YEARS_CHOICES,
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Phone Number'
                }
            )
        }


class EditProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'dob': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Date Of Birth'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Phone Number'
                }
            )
        }


class DeleteProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = AppUser
        fields = ()


class UserRegistrationForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = UserModel
        fields = ('email',)

        # def clean_first_name(self):
        #    return self.cleaned_data['first_name']

        # if you want to have user with profile together
        # def save(self, commit=True):
        #     user = super().save(commit=commit)
        #     profile = Profile(**self.cleaned_data(), user=user,)
        #     if commit:
        #         profile.save()
        #     return user
#
class UserChangeAdminForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields =('email',)
        # fields = ['email', 'password', 'is_active', 'is_staff', 'is_superuser',
        #           'groups', 'user_permissions', 'last_login']