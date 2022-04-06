from django.urls import path

from dentist_3_project.services.views import BlogView, build_services_view

urlpatterns = [
    path('blog/', BlogView.as_view(), name='show blog'),
    path('services/', build_services_view, name='show services'),
]