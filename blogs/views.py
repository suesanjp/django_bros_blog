from django.shortcuts import render
from .models import Blog

# Create your views here.


def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})

# class ModelDetailView(DetailView):
#     model = Model
#     template_name = ".html"


# class ModelListView(ListView):
#     model = Model
#     template_name = ".html"
