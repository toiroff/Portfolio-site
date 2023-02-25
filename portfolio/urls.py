from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',About,name="about"),
    path('portfolio/',portfolio,name="portfolio"),
    path('services/',Services,name="services"),
    path('contact/',contact,name="contact"),
    path('blog/',blog,name='blog'),
    path('blog-details/<str:pk>/',BlogDetails,name="blog-details")
]