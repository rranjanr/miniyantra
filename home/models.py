from django.db import models

# Create your models here.
class Event(models.Model): 
    title = models.CharField(max_length=300)
    description = models.TextField()
    price_pool = models.FloatField()
    thumbnail = models.ImageField(upload_to='img/')
    rulebook = models.FileField(upload_to='files/')
    reg_details = models.TextField(null=True,blank=True)

    def __str__(self): 
        return self.title


  
