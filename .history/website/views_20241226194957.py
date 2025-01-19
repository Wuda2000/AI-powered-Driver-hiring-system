from django.shortcuts import render
from django.http import JsonResponse

# Sample driver data
drivers = [
    {"name": "Eugene Mageto", "experience": 5, "image_url": "erik-lucatero-d2MSDujJl2g-unsplash.jpg"},
    {"name": "Sarah Mbuvi", "experience": 3, "image_url": "sarah-mbuvi.jpg"},
    {"name": "Collins Odhiambo", "experience": 8, "image_url": "collins-odhiambo.jpg"},
    {"name": "Jenevive Saru", "experience": 9, "image_url": "jenevive-saru.jpg"},

]

def index(request):
    return render(request, 'website/index.html')  # Ensure 'index.html' is inside 'website/templates/website/'
 

def get_drivers(request):
    return JsonResponse(drivers, safe=False)  # Returns the sample driver data as JSON
