from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    Pclass = int(request.form["Pclass"])
    Sex = int(request.form["Sex"])
    Age = float(request.form["Age"])
    SibSp = int(request.form["SibSp"])
    Parch = int(request.form["Parch"])
    Fare = float(request.form["Fare"])
    Embarked = int(request.form["Embarked"])

    prediction = model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])

    if prediction[0] == 1:
        result = "Passenger Survived"
    else:
        result = "Passenger Did Not Survive"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)