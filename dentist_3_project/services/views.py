from django.shortcuts import render

from django.views.generic import ListView

from dentist_3_project.services.models import BlogPost, Service


def build_services_view(request):
    restorative = Service.objects.filter(category__contains='2')
    preventative = Service.objects.filter(category__contains='1')
    cosmetic = Service.objects.filter(category__contains='3')

    context = {
        'restorative_services': restorative,
        'preventative_services': preventative,
        'cosmetic_services': cosmetic,
    }

    return render(request, 'services/services.html', context)



class BlogView(ListView):
    model = BlogPost
    template_name = 'services/blog.html'
