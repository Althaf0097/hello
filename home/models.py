from django.db import models

# makemigration - create change and store in a file 
# migrate - apply the pending changes create by makemigration 

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  email = models.EmailField(default="", blank=True)
  phone = models.CharField(max_length=122)
  desc = models.TextField(max_length=400)
  date = models.DateField()
  
  
  def __str__(self):
    return self.name
  
