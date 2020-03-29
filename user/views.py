from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'user/home.html')

def blog(request):
    return render(request, 'user/blog.html')

def blog_details(request):
    return render(request, 'user/single.html')

def about(request):
    return render(request, 'user/about.html')

def packages(request):
    return render(request, 'user/seo_packages.html')

def contact(request):
    return render(request, 'user/contact.html')

def testimonials(request):
    return render(request, 'user/testimonials.html')