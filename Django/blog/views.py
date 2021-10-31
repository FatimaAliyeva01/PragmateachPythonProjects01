from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request,'blog.html')
def about (request):
    return render(request,'about.html')
def about (request):
    return render(request,'home.html')

def blog_detail(request):
    user=[
        {
            "id" : "1",
            "ad" : "Fatima",
            "sinif" : "Flask"
        },
         {
            "id" : "2",
            "ad" : "Aydan",
            "sinif" : "Flask"
        },
         {
            "id" : "3",
            "ad" : "Fateh",
            "sinif" : "Flask"
        }
    ]
    return render(request, 'blog_detail.html', {'istifadeciler': users})