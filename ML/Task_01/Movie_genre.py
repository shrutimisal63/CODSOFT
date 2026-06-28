# ==============================
# Movie Genre Classification
# ==============================

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# Load Training Dataset
# -------------------------------

train_file = "train_data.txt"
test_file = "test_data.txt"
solution_file = "test_data_solution.txt"

train_df = pd.read_csv(
    train_file,
    sep=" ::: ",
    names=["ID", "TITLE", "GENRE", "PLOT"],
    engine="python"
)

print(train_df.head())

# -------------------------------
# Features and Labels
# -------------------------------

X = train_df["PLOT"]
y = train_df["GENRE"]

# -------------------------------
# Split Dataset
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# TF-IDF + Logistic Regression
# -------------------------------

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_features=50000
    )),
    ("classifier", LogisticRegression(
        max_iter=1000
    ))
])

# Train Model
model.fit(X_train, y_train)

# -------------------------------
# Prediction
# -------------------------------

predictions = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# -------------------------------
# Predict Test Dataset
# -------------------------------

test_file = "test_data.txt"

test_df = pd.read_csv(
    test_file,
    sep=" ::: ",
    names=["ID", "TITLE", "PLOT"],
    engine="python"
)

test_predictions = model.predict(test_df["PLOT"])

test_df["Predicted Genre"] = test_predictions

print(test_df.head())

# Save Predictions
test_df.to_csv("movie_genre_predictions.csv", index=False)

print("\nPredictions saved as movie_genre_predictions.csv")