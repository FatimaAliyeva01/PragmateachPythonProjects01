from django.urls import path
from .views import (index,
    blog_list,
    blog_detail,
    about
    )

app_name = 'blog'

urlpatterns = [
    path('home/', index, name='index'),
    path('', blog_list, name='blog-list'),
    path('blog-detail/<slug:slug>/', blog_detail, name='blog-detail' ),
    path('about/', about, name='about'),
]
