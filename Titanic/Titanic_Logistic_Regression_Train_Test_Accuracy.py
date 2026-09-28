import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Titanic dataset
data = pd.read_csv("Titanic/train.csv")

# Select features
X = data[["Pclass", "Age", "Fare"]]

# Result: 0 = Not Survived, 1 = Survived
y = data["Survived"]

# Handle missing values
X = X.fillna(X.mean())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# New passenger
new_passenger = pd.DataFrame(
    [[3, 25, 10]],
    columns=["Pclass", "Age", "Fare"]
)

prediction = model.predict(new_passenger)
probability = model.predict_proba(new_passenger)

print("Prediction:", prediction)
print("Probability:", probability)