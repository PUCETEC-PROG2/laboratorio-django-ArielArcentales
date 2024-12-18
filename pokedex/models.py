from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=40, null= False)
    type = models.CharField(max_length=40, null= False)
    weigth = models.DecimalField(max_digits=10,decimal_places=2)
    heigth = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
    
