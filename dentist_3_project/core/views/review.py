from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from dentist_3_project.core.forms import ReviewForm, EditReviewForm, DeleteReviewForm
from dentist_3_project.core.models import Review, Appointment


class AllReviewsView(ListView, LoginRequiredMixin):
    model = Review
    template_name = 'core/reviews-all.html'

    # TODO
    # FIX THIS ---> this disables after click , but for all other reviews as well
    # it needs to disable only for the single review that is clicked on
    # it will work on a Details view
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(AllReviewsView, self).get_context_data()
    #
    #     clicked = self.request.session['clicked'] = False
    #     context['clicked'] = clicked
    #     return context

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


def like_review(request, pk):
    review = Review.objects.get(pk=pk)
    review.likes += 1
    request.session['clicked'] = True
    review.save()
    return redirect('show all reviews')


def dislike_review(request, pk):
    review = Review.objects.get(pk=pk)
    review.dislikes += 1
    request.session['clicked'] = True
    review.save()

    return redirect('show all reviews')