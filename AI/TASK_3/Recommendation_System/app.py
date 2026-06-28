from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load movie data
movies = pd.read_csv("movies.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    recommendation = []

    if request.method == "POST":
        genre = request.form["genre"]

        recommendation = movies[movies["Genre"].str.lower() == genre.lower()]
        recommendation = recommendation["Movie"].tolist()

    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)