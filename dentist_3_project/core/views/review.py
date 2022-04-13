from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

from dentist_3_project.core.forms import ReviewForm, EditReviewForm, DeleteReviewForm
from dentist_3_project.core.models import Review, Appointment

class AllReviewsView(ListView):
    model = Review
    template_name = 'core/reviews-all.html'


@login_required
def build_add_review(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.appointment = appointment
            form.save()
            return redirect('show profile view', pk=request.user.id)

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'core/review-add.html', context)


@login_required
def build_edit_review(request, pk):
    rev = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditReviewForm(request.POST, instance=rev)
        if form.is_valid():
            form.save()
            return redirect('show profile view', pk=request.user.id)

    else:
        form = EditReviewForm(instance=rev)

    context = {
        'form': form,
        'rev': rev
    }

    return render(request, 'core/review-edit.html', context)


@login_required
def build_delete_review(request, pk):
    rev = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteReviewForm(request.POST, instance=rev)
        if form.is_valid():
            form.save()
            return redirect('show profile view', pk=request.user.id)

    else:
        form = DeleteReviewForm(instance=rev)

    context = {
        'form': form,
        'rev': rev
    }

    return render(request, 'core/review-delete.html', context)