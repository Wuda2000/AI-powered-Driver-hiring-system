from django.shortcuts import render
from django.http import JsonResponse

# Sample driver data
drivers = [

      {

        "name": "Eugene Mageto",
         "experience": 5,
         "image_url": "erik-lucatero-d2MSDujJl2g-unsplash.jpg"
        },
    {
        "name": "Sarah Mbuvi",
        "experience": 3,
        "image_url": "gabriel-silverio-u3WmDyKGsrY-unsplash.jpg"
    },
    {
        "name": "Collins Odhiambo",
        "experience": 8,
        "image_url": "jimmy-fermin-bqe0J0b26RQ-unsplash.jpg"
    },
    {
        "name": "Jenevive Saru",
        "experience": 9,
        "image_url": "ludvig-wiese-d-MfHM-jHwc-unsplash.jpg"
    }
]
def index(request):
    return render(request, 'website/index.html', {'drivers': drivers})

def get_drivers(request):
    return JsonResponse(drivers, safe=False)  # This returns the driver data as JSON

# New views for additional pages
def about_us_view(request):
    return render(request, 'website/.html')

def services_view(request):
    return render(request, 'website/Services.html')

def pricing_view(request):
    return render(request, 'website/Pricing.html')

def clients_view(request):
    return render(request, 'website/clients.html')

def contact_view(request):
    return render(request, 'contact.html')