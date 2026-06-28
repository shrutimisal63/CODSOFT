import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Read CSV file
df = pd.read_csv("IRIS.csv")   # put your file name here

# 2. Show data
print(df.head())

# 3. Split features and target
X = df.drop("species", axis=1)   # input columns
y = df["species"]                # output column

# 4. Convert text labels into numbers
le = LabelEncoder()
y = le.fit_transform(y)

# 5. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Create model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# 7. Predict
y_pred = model.predict(X_test)

# 8. Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# 9. Test with new data
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("Predicted species:", le.inverse_transform(prediction)[0])