from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home/homepage.html')

def aboutus(request):
  return render(request,'home/aboutus.html' )

def sponsor(request):
  return render(request, 'home/sponsor.html')

def event(request):
  return render(request, 'home/event.html')

def register(request):
  return render(request, 'home/register.html')

def aboutrobotics(request):
  return render(request, 'home/aboutrobotics.html')

def aboutautomation(request):
  return render(request, 'home/aboutautomation.html')

def ai_hackathon(request):
  return render(request, 'home/ai_hackathon.html')
