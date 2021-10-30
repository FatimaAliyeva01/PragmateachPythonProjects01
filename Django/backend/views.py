from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Model-View-Controller
# def home(request):
#     return HttpResponse ('<h1>My first web site</h1>')

def about(request):
     return HttpResponse ('<h1> About this page </h1>')
def home(request):
     return render(request,'home.html')