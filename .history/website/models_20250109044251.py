from django.db import models

class CarOwner(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price_per_day = models.FloatField()
    rating = models.FloatField()
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    mileage = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.car_make} {self.car_model} ({self.car_year})"
