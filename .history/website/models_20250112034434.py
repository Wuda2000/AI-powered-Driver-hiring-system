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
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_make} {self.car_model} ({self.car_year})"
    

    class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    profile_visibility = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s settings"
