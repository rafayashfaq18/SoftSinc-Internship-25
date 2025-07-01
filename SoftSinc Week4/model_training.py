import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def load_data(filepath, target_column):
    print(f" Loading data from: {filepath}")
    try:
        df = pd.read_csv(filepath)
        print(" Data loaded successfully!")
        print(" First 5 rows:\n", df.head())
        X = df.drop(target_column, axis=1)
        y = df[target_column]
        print(f" Target column: {target_column}")
        print(f" Features shape: {X.shape}, Labels shape: {y.shape}")
        return X, y
    except FileNotFoundError:
        print(" File not found. Please check your path.")
        exit()
    except Exception as e:
        print(" Error loading data:", str(e))
        exit()

def preprocess(X):
    print("\n Preprocessing numerical features...")
    try:
        scaler = StandardScaler()
        numeric_columns = X.select_dtypes(include=np.number).columns
        X_scaled = scaler.fit_transform(X[numeric_columns])
        print(" Features scaled.")
        return X_scaled
    except Exception as e:
        print(" Error during preprocessing:", str(e))
        exit()

def train_and_save_model(X, y, model, model_path):
    print("\n Training the model...")
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        print(" Model trained successfully!")
        print(" Accuracy on test data:", round(accuracy * 100, 2), "%")

        # Save model
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        joblib.dump(model, model_path)
        print(f" Model saved to: {model_path}")
    except Exception as e:
        print(" Error during model training:", str(e))
        exit()

# This runs only when you run the file directly
if __name__ == "__main__":
    print(" Starting ML training pipeline...")
    X, y = load_data("data/iris.csv", "species")
    X_scaled = preprocess(X)
    model = RandomForestClassifier()
    train_and_save_model(X_scaled, y, model, "models/model_classification.pkl")
    print(" Done!")
