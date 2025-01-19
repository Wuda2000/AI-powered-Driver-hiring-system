from django.shortcuts import render
from django.http import JsonResponse
import joblib
from .models import CarOwner
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os


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
    context = {} 
    return render(request, '')
 # Add any context data if needed
    return render(request, 'website/car-owners-offer.html', context)  # Make sure you return a valid response

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
model = joblib.load('car_owners_model.pkl')


MODEL_PATH = os.path.join(os.path.dirname(__file__), 'car_owners_model.pkl')
car_owner_model = None

def load_model():
    global car_owner_model
    if car_owner_model is None:
        with open(MODEL_PATH, 'rb') as model_file:
            car_owner_model = pickle.load(model_file)
    return car_owner_model

def recommend_car_owners(request):
    try:
        # Load car owner data
        car_owners = CarOwner.objects.all()

        # Prepare features for prediction
        features = pd.DataFrame.from_records(
            [
                {
                    "price_per_day": owner.price_per_day,
                    "rating": owner.rating,
                    "car_make": owner.car_make,
                    "car_model": owner.car_model,
                    "car_year": owner.car_year,
                    "mileage": owner.mileage,
                    "location": owner.location,
                }
                for owner in car_owners
            ]
        )
        features = pd.get_dummies(features)

        # Predict using the model
        model = load_model()
        predictions = model.predict(features)

        # Annotate car owners with predictions
        for owner, prediction in zip(car_owners, predictions):
            owner.is_high_paying = prediction  # Add a temporary attribute for display

        return render(request, 'website/car_owners_offer.html', {'recommended_owners': car_owners})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

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


# Load the trained model
def load_model():
    with open('car_owners_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Use the model to predict whether a car owner is high paying
def predict_high_paying(car_owner_data):
    model = load_model()
    
    # Convert the car owner data to the same format used for training
    car_owner_df = pd.DataFrame([car_owner_data])
    car_owner_df = pd.get_dummies(car_owner_df)
    
    # Predict if the car owner is high paying
    prediction = model.predict(car_owner_df)
    
    # Return the prediction (1 = high paying, 0 = not high paying)
    return prediction[0]

# View to handle displaying and predicting car owners
def recommend_car_owners(request):
    car_owner_data = {
        'price_per_day': 50,  # Example input data
        'rating': 4.5,
        'car_make': 'Toyota',
        'car_model': 'Camry',
        'car_year': 2020,
        'mileage': 15000,
        'location': 'New York',
    }

    # Get prediction for the car owner
    is_high_paying = predict_high_paying(car_owner_data)

    return render(request, 'website/car_owners_offer.html', {'is_high_paying': is_high_paying})
# Assuming you have a model named CarOwner and a function to fetch recommended car owners
from .models import CarOwner

def car_owners_offer(request):
    # Fetch recommended car owners from your database or model
   recommended_owners = CarOwner.objects.filter(rating__gte=4)  # Example filter based on rati
   return render(request, 'car-owners-offer.html', {'recommended_owners': recommended_owners})