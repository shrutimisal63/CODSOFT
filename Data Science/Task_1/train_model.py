import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import joblib

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

# Drop unwanted columns
df = df.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Encode categorical columns
le = LabelEncoder()

df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])

# -------------------------
# Graph 1 Survival Count
# -------------------------

plt.figure(figsize=(5,4))
df["Survived"].value_counts().plot(kind="bar",color=["red","green"])
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Passengers")
plt.savefig("survival_count.png")
plt.show()

# -------------------------
# Graph 2 Male Female
# -------------------------

plt.figure(figsize=(5,4))
df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender Count")
plt.savefig("gender_count.png")
plt.show()

# -------------------------
# Graph 3 Age Distribution
# -------------------------

plt.figure(figsize=(6,4))
plt.hist(df["Age"],bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("age_distribution.png")
plt.show()

# Features

X = df.drop("Survived",axis=1)
y = df["Survived"]

X_train,X_test,y_train,y_test=train_test_split(
X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,y_train)

pred=model.predict(X_test)

print("\nAccuracy:",accuracy_score(y_test,pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test,pred))

print("\nClassification Report")
print(classification_report(y_test,pred))

joblib.dump(model,"model.pkl")

print("\nModel Saved Successfully.")