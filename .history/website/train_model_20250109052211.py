import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
def load_data():
    return pd.read_csv('car_owners_data.csv')

def train_model():
    df = load_data()

    # Features and labels
    X = df[['price_per_day', 'rating', 'car_make', 'car_model', 'car_year', 'mileage', 'location']]
    X = pd.get_dummies(X)  # Encode categorical data
    y = df['high_paying (target)']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate accuracy
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    # Save the model
    with open('car_owners_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    print("Model saved as 'car_owners_model.pkl'")

# Run the training script
if __name__ == "__main__":
    train_model()
