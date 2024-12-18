from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('sponsor/', views.sponsor,name='sponsor'),
    path('event/', views.event,name='event'),
    path('register/', views.register,name='register'),

]