from django.urls import path, include

from dentist_3_project.core.views.appointment import build_book_appointment, build_delete_appointment, \
    build_appointment_details
from dentist_3_project.core.views.generic import HomeView, ContactsView
from dentist_3_project.core.views.review import build_add_review, build_edit_review, build_delete_review, AllReviewsView

urlpatterns = [
    path('', HomeView.as_view(), name='show index'),
    path('contacts/', ContactsView.as_view(), name='show contacts'),
    path('book-appointment/', build_book_appointment, name='show book appointment'),
    path('delete-appointment/<int:pk>/', build_delete_appointment, name='show delete appointment'),
    path('appointment-details/<int:pk>', build_appointment_details, name='show appointment details'),

    path('add-review/<int:pk>', build_add_review, name='show add review'),
    path('edit-review/<int:pk>/', build_edit_review, name='show edit review'),
    path('delete-review/<int:pk>/', build_delete_review, name='show delete review'),
    path('all-reviews/', AllReviewsView.as_view(), name='show all reviews'),



]