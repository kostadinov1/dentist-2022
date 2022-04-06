from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from dentist_3_project.services.models import BlogPost, Service

# class ServicesView(ListView):
#     pass
#


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


# from django.views import generic
# from .models import Post
#
# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#
