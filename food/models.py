from django.db import models
    
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price =models.CharField(max_length=200)
    image =models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name