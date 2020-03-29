

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about-us/',views.about,name='about'),
    path('seo-packages/',views.packages, name='seo-packages'),
    path('testimonials/',views.testimonials, name='testimonials'),
    path('blog/',views.blog,name='blog'),
    path('blog-details/',views.blog_details,name='blog-details'),
    path('contact/',views.contact,name='contact'),
]