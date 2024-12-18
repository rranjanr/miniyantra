from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('sponsor/', views.sponsor,name='sponsor'),
    path('event/', views.event,name='event'),
    path('register/', views.register,name='register'),
    path('aboutrobotics/', views.aboutrobotics,name='aboutrobotics'),
    path('aboutautomation/', views.aboutautomation,name='aboutautomation'),
    path('aboutai_hackathon/', views.ai_hackathon,name='aboutai_hackathon'),

]