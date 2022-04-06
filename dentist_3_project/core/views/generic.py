from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/index.html'



class ContactsView(TemplateView):
    template_name = 'core/contacts.html'


