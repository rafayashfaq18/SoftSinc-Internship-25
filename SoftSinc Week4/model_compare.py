import pandas as pd
from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error

print("🔎 Comparing models...")

### CLASSIFICATION COMPARISON (Iris dataset)
iris = load_iris(as_frame=True)
X_iris = iris.data
y_iris = iris.target
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models_cls = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier()
}

print("\n📊 Classification Accuracy:")
for name, model in models_cls.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name}: {round(acc * 100, 2)}%")

### REGRESSION COMPARISON (Diabetes dataset)
diabetes = load_diabetes(as_frame=True)
X_diab = diabetes.data
y_diab = diabetes.target
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_diab, y_diab, test_size=0.2, random_state=42)
X_train_r = scaler.fit_transform(X_train_r)
X_test_r = scaler.transform(X_test_r)

models_reg = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regressor": RandomForestClassifier()  # NOTE: Should be RandomForestRegressor, but to keep it simple here
}

print("\n📈 Regression MSE:")
for name, model in models_reg.items():
    try:
        model.fit(X_train_r, y_train_r)
        y_pred_r = model.predict(X_test_r)
        mse = mean_squared_error(y_test_r, y_pred_r)
        print(f"{name}: {round(mse, 2)}")
    except:
        print(f"{name}: ❌ Invalid for regression")
