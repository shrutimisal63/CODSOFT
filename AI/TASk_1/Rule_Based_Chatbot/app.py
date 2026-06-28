from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    user = request.json["message"].lower()

    if "hello" in user or "hi" in user or "hey" in user:
        reply = "👋 Hello! Welcome to the Rule-Based Chatbot."

    elif "how are you" in user:
        reply = "😊 I'm doing great! Thanks for asking."

    elif "your name" in user:
        reply = "🤖 My name is SmartBot."

    elif "time" in user:
        reply = "🕒 Current Time: " + datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        reply = "📅 Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    elif "weather" in user:
        reply = "☀️ I can't check live weather, but I hope it's sunny!"

    elif "joke" in user:
        reply = "😂 Why do programmers prefer dark mode? Because light attracts bugs!"

    elif "creator" in user or "created" in user:
        reply = "👨‍💻 I was created using Python, Flask, HTML, CSS, and JavaScript."

    elif "help" in user:
        reply = """
I can answer:
• Hello
• Time
• Date
• Joke
• Weather
• Calculator
• Name
"""

    elif "calculate" in user:
        try:
            expression = user.replace("calculate", "")
            answer = eval(expression)
            reply = f"🧮 Answer = {answer}"
        except:
            reply = "Please enter like: calculate 5+4"

    elif "bye" in user:
        reply = "👋 Goodbye! Have a wonderful day."

    else:
        reply = "❌ Sorry, I don't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)