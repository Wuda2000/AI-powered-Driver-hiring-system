from django.shortcuts import render
from django.http import JsonResponse
import joblib
from django.shortcuts import render
from .models import CarOwner

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
    return render(request, 'website/Aboutus.html')

def services_view(request):
    return render(request, 'website/Services.html')

def pricing_view(request):
    return render(request, 'website/Pricing.html')

def clients_view(request):
    return render(request, 'website/clients.html')

def contact_view(request):
    return render(request, 'website/contact.html')
# View for Car Owners Offer Page
def car_owners_offer(request):
    return render(request, 'website/car-owners-offer.html')

# View for Drivers Offer Page
def drivers_offer(request):
    return render(request, 'website/drivers-offer.html')

# View for Objective Page
def objective(request):
    return render(request, 'website/objective.html')

# View for Feedback Page
def feedback(request):
    return render(request, 'website/feedback.html')

# View for Ratings Page
def ratings(request):
    return render(request, 'website/ratings.html')


# Load your trained machine learning model (e.g., a pickled model)
model = joblib.load('path_to_your_trained_model.pkl')

def recommend_car_owners(request):
    # Get all car owners from the database
    car_owners = CarOwner.objects.all()
    
    # Prepare the features for prediction (for example, price_per_day and rating)
    features = [(owner.price_per_day, owner.rating) for owner in car_owners]
    
    # Use the model to predict scores for each car owner
    predictions = model.predict(features)
    
    # Add the prediction score to each car owner (this is optional, for analysis)
    for i, owner in enumerate(car_owners):
        owner.prediction_score = predictions[i]  # You can store this score in the database if needed
    
    # Sort car owners by the predicted score (descending)
    recommended_owners = sorted(car_owners, key=lambda x: x.prediction_score, reverse=True)
    
    # Render the template with the recommended owners
    return render(request, 'car_owners_offers.html', {'recommended_owners': recommended_owners})