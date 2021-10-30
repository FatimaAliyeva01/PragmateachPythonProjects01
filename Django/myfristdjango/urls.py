"""myfristdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views as backend_views
from blog import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',backend.views.home),
#     # path('about/',views.about, name="Aboutpage")
#     #Yaratdigimiz applari burda qeyd ediriq

# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_list),
    path('about/',backend_views.about),
    path('blog/', views.about )
    #Yaratdigimiz applari burda qeyd ediriq.
    #burdakilar funksiyalr name ise funsksiylara adlandirma

]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('Blog/', views.blog_list)
# ]