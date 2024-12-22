from django.contrib import admin
from .models import Registration, Event

# Register your models here
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  list_display =('id','title', 'description', 'price_pool', 'thumbnail', 'rulebook', 'reg_details')
  

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'college', 'phone_number', 'area_of_intrest')