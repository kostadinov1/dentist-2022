from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from dentist_3_project.accounts.forms import UserRegistrationForm, CreateProfileForm, EditProfileForm, DeleteProfileForm
from dentist_3_project.accounts.models import Profile, AppUser
from dentist_3_project.core.models import Review, Appointment

UserModel = get_user_model()


class ProfileDetailsView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'auth/profile-view.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(user_id=self.request.user)
        context['appointments'] = Appointment.objects.filter(user_id=self.request.user)
        context['user'] = self.request.user

        return context


class CreateUserProfileView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('show index')
    form_class = CreateProfileForm
    template_name = 'auth/profile-create.html'
    success_url = reverse_lazy('show index')
    success_message = 'New user profile has been created'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'auth/profile-edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('show profile view', kwargs={'pk': self.object.user.id})


class DeleteProfileView(DeleteView, LoginRequiredMixin):
    model = AppUser
    template_name = 'auth/profile-delete.html'
    success_url = reverse_lazy('show index')
    form_class = DeleteProfileForm


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('show index')

    # to log us in straight after registration
    def form_valid(self, form):   # *args, **kwargs to be more extensible
        result = super().form_valid(form)
        # user -> self.object
        # req -> self.request
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    # this method needs to be overrided
    def get_success_url(self):
        return reverse_lazy('show index')


@login_required
def build_logout(request):
    logout(request)
    # messages.info(request, 'LOG OUT SUCCESSFUL')
    return redirect('show index')


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    success_url = reverse_lazy('show sign in')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'auth/login.html'
