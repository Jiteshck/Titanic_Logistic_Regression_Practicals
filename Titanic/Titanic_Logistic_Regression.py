import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load Titanic dataset
data = pd.read_csv("Titanic/train.csv")

# Select features
X = data[["Pclass", "Age", "Fare"]]

# Result: 0 = Not Survived, 1 = Survived
y = data["Survived"]

# Handle missing values
X = X.fillna(X.mean())

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict for a passenger
new_passenger = pd.DataFrame(
    [[3, 25, 10]],
    columns=["Pclass", "Age", "Fare"]
)

prediction = model.predict(new_passenger)

print("Prediction:", prediction)

# Probability
probability = model.predict_proba(new_passenger)

print("Probability:", probability)