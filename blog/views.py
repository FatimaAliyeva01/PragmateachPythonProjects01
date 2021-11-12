from django.shortcuts import  get_object_or_404,render

# Create your views here.
from .models import Blog

def index(request):
    return render(request, 'index.html', )


def blog_list(request):
    blogs = Blog.objects.all()
    customers = [
        {
            'ad': 'Con', 
            'soyad': 'Terry'
        }, 
        {
            'ad': 'Ali', 
            'soyad': 'Aliyev'
        }
    ]
    context = {
        'blogs': blogs,
        'customers': customers,
        }

    return render(request, 'blogs.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-detail.html', {'blog': blog})

def about(request):
    return render(request, 'about.html')

