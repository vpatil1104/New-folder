from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("q", views.q, name="q"),
    
    path("", views.contact, name="contactus"),

 
]