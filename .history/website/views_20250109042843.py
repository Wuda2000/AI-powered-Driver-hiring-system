from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .models import CarOwner
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle


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
    return render(request, 'website/car_owners_offers.html', {'recommended_owners': recommended_owners})

# Load the CSV file into a pandas DataFrame
def load_data():
    df = pd.read_csv('car_owners_data.csv')
    return df

# Prepare data for training
def train_model():
    df = load_data()
    
    # Features (columns used for prediction)
    X = df[['price_per_day', 'rating', 'car_make', 'car_model', 'car_year', 'mileage', 'location']]
    
    # Convert categorical columns (car_make, car_model, and location) into numerical values using pd.get_dummies
    X = pd.get_dummies(X)
    
    # Target (high_paying column)
    y = df['high_paying']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a RandomForestClassifier model (you can try other models like Logistic Regression, SVM, etc.)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')
    
    # Save the trained model using pickle
    with open('car_owners_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

train_model()



def recommend_car_owner(request):
    # Example car owner data to predict (you can get this from user input or your database)
    car_owner_data = {
        'price_per_day': 50,
        'rating': 4.5,
        'car_make': 'Toyota',
        'car_model': 'Camry',
        'car_year': 2020,
        'mileage': 15000,
        'location': 'New York'
    }
    
    # Predict if this car owner is high paying
    result = predict_high_paying(car_owner_data)
    
    # Render the result to the template
    return render(request, 'werecommendation_result.html', {'result': result})
