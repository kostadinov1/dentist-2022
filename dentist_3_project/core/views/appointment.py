from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from dentist_3_project.core.forms import AppointmentForm, DeleteAppointmentForm
from dentist_3_project.core.models import Appointment, Review


@login_required
def build_book_appointment(request):
    user = request.user
    try:
        profile = request.user.profile

    except:
        messages.info(request, 'Please create Your Profile first.')
        return redirect('show profile create')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            venue = form.cleaned_data['venue']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']

            form = form.save(commit=False)
            form.user = request.user
            name = form.user.profile.first_name
            phone = form.user.profile.phone
            email = form.user.email
            send_mail(f'Appointment from {name} at {date}{time} at {venue} with phone number: {phone} and email: {email}',
                      message, f'{email}', ['evgenikostadinov1987@gmail.com'],)
            form.save()
            return redirect('show profile view', user.id)
    else:
        form = AppointmentForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'core/appointment.html', context)


@login_required
def build_appointment_details(request, pk):
    appo = Appointment.objects.get(pk=pk)
    reviewed = Review.objects.filter(appointment=appo)


    context = {
        'appo': appo,
        'reviewd': reviewed,
    }

    return render(request, 'core/appointment-details.html', context)


@login_required
def build_delete_appointment(request, pk):
    appoint = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAppointmentForm(request.POST, instance=appoint)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAppointmentForm(instance=appoint)

    context = {
        'form': form,
        'appoint': appoint,
    }

    return render(request, 'core/appointment_delete.html', context)
