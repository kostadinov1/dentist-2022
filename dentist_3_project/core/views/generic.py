from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/index.html'

    # tried to cache the page with no success. --- HAVE A LOOK AGAIN ---
    # @method_decorator(cache_page(60 * 5), name='dispatch')
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


class ContactsView(TemplateView):
    template_name = 'core/contacts.html'


