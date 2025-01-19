from django.shortcuts import render
from django.http import JsonResponse

# Sample driver data
drivers = [
    {"name": "John Doe", "experience": 5},
    {"name": "Jane Smith", "experience": 3},
    {"name": "James Brown", "experience": 8},
]

def index(request):
    return render(request, 'index.html')  # Make sure index.html exists in templates

def get_drivers(request):
    return JsonResponse(drivers, safe=False)  # Returns the sample driver data as JSON
