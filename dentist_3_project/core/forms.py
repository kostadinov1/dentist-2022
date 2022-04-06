import datetime

from django import forms

from dentist_3_project.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from dentist_3_project.core.models import Appointment, Review
YEARS_CHOICES = range(datetime.date.today().year, datetime.date.today().year + 1)


class AppointmentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Appointment
        exclude = ('user', )
        widgets={
            'date': forms.SelectDateWidget(
                years= YEARS_CHOICES,
            ),
            'message': forms.TextInput(attrs={'rows': 4})
        }


class DeleteAppointmentForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Appointment
        exclude = ('user', 'tagged_reviews')


class ReviewForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.appointment = appointment
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        exclude = ('user', 'appointment')


class EditReviewForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Review
        exclude = ('user', 'appointment')


class DeleteReviewForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    def save(self):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Review
        exclude = ('user', 'appointment')
