# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
# Replace 'spam.csv' with your dataset filename
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only required columns (for Kaggle SMS Spam dataset)
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Convert labels into numbers
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Features and Target
X = data['message']
y = data['label']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# Test Custom SMS
while True:
    sms = input("\nEnter SMS (or type 'exit'): ")

    if sms.lower() == "exit":
        break

    sms_vector = vectorizer.transform([sms])
    prediction = model.predict(sms_vector)

    if prediction[0] == 1:
        print("Spam SMS")
    else:
        print("Legitimate SMS")