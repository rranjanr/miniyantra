from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
  return render(request, 'home/homepage.html')

def aboutus(request):
  return render(request,'home/aboutus.html' )

def sponsor(request):
  return render(request, 'home/sponsor.html')

def event(request):
  events = Event.objects.all()
  context = {   
    'events':events
  }
  return render(request, 'home/event.html',context)

def register(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    college = request.POST.get('college')
    number = request.POST.get('number')
    reg_type = request.POST.get('reg_type')
    reg_info = Registration.objects.create(
      name = name,
      college = college,
      phone_number = number,
      area_of_intrest = reg_type
    )
    messages.success(request,'Registration Successful')
    return redirect('homepage')
  return render(request, 'home/register.html')

def aboutrobotics(request):
  return render(request, 'home/aboutrobotics.html')

def aboutautomation(request):
  return render(request, 'home/aboutautomation.html')

def ai_hackathon(request):
  return render(request, 'home/ai_hackathon.html')
