# Titanic Logistic Regression Practicals

This project contains two practical programs demonstrating **Logistic Regression** using the Titanic dataset with Python and Scikit-learn.

The programs predict whether a Titanic passenger **Survived or did not Survive** based on passenger information.

## 📌 Project Overview

- **Input:** Passenger information
- **Output:** Survival prediction
- `0` → Not Survived
- `1` → Survived

The project contains two practical programs:

1. Basic Logistic Regression
2. Logistic Regression with Train-Test Split and Accuracy Evaluation

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Train-Test Split
- Accuracy Score

---

## 📂 Project Structure

```text
├── Titanic_Logistic_Regression.py
├── Titanic_Logistic_Regression_Train_Test_Accuracy.py
├── train.csv
├── test.csv
├── Titanic_Logistic_Regression_Practicals.pdf
└── README.md
````

---

## 📘 Practical 1 — Basic Logistic Regression

### File

`Titanic_Logistic_Regression.py`

This program uses the Titanic dataset to train a Logistic Regression model.

The following features are used:

* `Pclass` → Passenger class
* `Age` → Passenger age
* `Fare` → Ticket fare

The target variable is:

* `0` → Not Survived
* `1` → Survived

Missing values in the selected features are handled using the mean value.

The model is then trained using the Titanic dataset and used to predict the survival of a new passenger.

### Example Passenger

```text
Pclass = 3
Age = 25
Fare = 10
```

The program displays:

* Prediction
* Probability of Not Surviving
* Probability of Surviving

### Concepts Covered

* Loading a CSV dataset
* Selecting features
* Handling missing values
* Logistic Regression
* Model training
* Prediction
* Prediction probability

---

## 📗 Practical 2 — Train-Test Split and Accuracy

### File

`Titanic_Logistic_Regression_Train_Test_Accuracy.py`

This program extends the first practical by dividing the Titanic dataset into training and testing data.

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

The model is trained using the training data and evaluated using the test data.

The accuracy of the model is calculated using:

```python
accuracy_score()
```

The program also predicts the survival of a new passenger and displays the prediction probability.

### Concepts Covered

* Train-Test Split
* Logistic Regression
* Model training
* Test data prediction
* Accuracy evaluation
* Prediction probability

---

## 🔄 Machine Learning Workflow

### Practical 1

```text
Titanic Dataset
       ↓
Select Features
       ↓
Handle Missing Values
       ↓
Logistic Regression
       ↓
Prediction
       ↓
Probability
```

### Practical 2

```text
Titanic Dataset
       ↓
Select Features
       ↓
Handle Missing Values
       ↓
Train-Test Split
       ↓
Logistic Regression
       ↓
Prediction
       ↓
Accuracy
       ↓
Probability
```

---

## 📊 Features Used

| Feature  | Description     |
| -------- | --------------- |
| `Pclass` | Passenger class |
| `Age`    | Passenger age   |
| `Fare`   | Ticket fare     |

### Target

| Value | Meaning      |
| ----: | ------------ |
|   `0` | Not Survived |
|   `1` | Survived     |

---


## 📄 Practical Documentation

The complete code and output for both practicals are available in:

```text
Titanic_Logistic_Regression_Practicals.pdf
```

---

## 🎯 Learning Outcomes

This practical demonstrates:

* Understanding Logistic Regression
* Working with a real-world dataset
* Loading CSV data
* Feature selection
* Handling missing values
* Training a machine learning model
* Making predictions
* Predicting probabilities
* Train-Test Split
* Model accuracy evaluation

---
