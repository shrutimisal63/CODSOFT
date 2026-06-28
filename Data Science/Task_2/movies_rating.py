import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("IMDb Movies India.csv", encoding="latin1")

df.columns = df.columns.str.strip()

print("First 5 rows:")
print(df.head())

# -------------------------------
# Clean Target (Rating)
# -------------------------------

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df = df.dropna(subset=["Rating"])

# -------------------------------
# Feature Engineering
# -------------------------------

# Convert Votes to numeric
df["Votes"] = df["Votes"].astype(str).str.replace(",", "")
df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")
df["Votes"] = df["Votes"].fillna(df["Votes"].median())

# Extract Year
df["Year"] = df["Year"].astype(str).str.extract(r"(\d{4})")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Year"] = df["Year"].fillna(df["Year"].median())

# Fill categorical missing values
categorical_features = ["Genre", "Director", "Actor 1", "Actor 2", "Actor 3"]

for col in categorical_features:
    df[col] = df[col].fillna("Unknown")

# -------------------------------
# Define Features & Target
# -------------------------------

X = df[categorical_features + ["Votes", "Year"]]
y = df["Rating"]

numeric_features = ["Votes", "Year"]

# -------------------------------
# Preprocessing
# -------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        ("num", SimpleImputer(strategy="median"), numeric_features),
        ("cat", Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]), categorical_features)
    ]
)

# -------------------------------
# Model
# -------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

# -------------------------------
# Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------

pipeline.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------

y_pred = pipeline.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------

print("\nModel Performance:")
print("MAE  :", mean_absolute_error(y_test, y_pred))
print("RMSE :", mean_squared_error(y_test, y_pred) ** 0.5)
print("R2   :", r2_score(y_test, y_pred))

# -------------------------------
# Results Table
# -------------------------------

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nSample Predictions:")
print(result.head(15))

# -------------------------------
# Plot
# -------------------------------

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Rating")
plt.ylabel("Predicted Rating")
plt.title("Actual vs Predicted Ratings")
plt.grid(True)
plt.show()