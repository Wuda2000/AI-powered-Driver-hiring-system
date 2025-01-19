from django.db import models

class CarOwner(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    price_per_day = models.FloatField()
    rating = models.FloatField()
    
    def __str__(self):
        return self.name
