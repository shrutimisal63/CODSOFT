# ==========================================
# CUSTOMER CHURN PREDICTION
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# ------------------------------------------
# Load Dataset
# ------------------------------------------
df = pd.read_csv("Churn_Modelling.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# Remove Unnecessary Columns
# ------------------------------------------
df.drop(["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)

# ------------------------------------------
# Encode Categorical Columns
# ------------------------------------------
le = LabelEncoder()

categorical_columns = ["Geography", "Gender"]

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# ------------------------------------------
# Features and Target
# ------------------------------------------
X = df.drop("Exited", axis=1)
y = df["Exited"]

# ------------------------------------------
# Train-Test Split
# ------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ------------------------------------------
# Models
# ------------------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    )
}

best_model = None
best_accuracy = 0
best_prediction = None

# ------------------------------------------
# Train & Evaluate
# ------------------------------------------
for name, model in models.items():

    print("\n====================================")
    print(name)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", round(accuracy * 100, 2), "%")

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_prediction = y_pred

# ------------------------------------------
# Best Model
# ------------------------------------------
print("\n====================================")
print("Best Model:", type(best_model).__name__)
print("Best Accuracy:", round(best_accuracy * 100, 2), "%")

# ------------------------------------------
# Confusion Matrix
# ------------------------------------------
cm = confusion_matrix(y_test, best_prediction)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ------------------------------------------
# Feature Importance
# ------------------------------------------
if hasattr(best_model, "feature_importances_"):

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": best_model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    plt.figure(figsize=(8,6))
    sns.barplot(
        data=importance,
        x="Importance",
        y="Feature"
    )
    plt.title("Feature Importance")
    plt.show()

# ------------------------------------------
# Save Best Model (Optional)
# ------------------------------------------
import joblib

joblib.dump(best_model, "customer_churn_model.pkl")

print("\nBest model saved as customer_churn_model.pkl")