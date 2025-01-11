from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample workout data
workouts = {
    "beginner": ["10 push-ups", "15 squats", "20 jumping jacks"],
    "intermediate": ["20 push-ups", "25 squats", "30 jumping jacks"],
    "advanced": ["30 push-ups", "40 squats", "50 jumping jacks"]
}

@app.route("/")
def home():
    return "Welcome to Fitness AI Chatbot! Use /chat to interact."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    if "workout" in user_message:
        if "beginner" in user_message:
            response = workouts["beginner"]
        elif "intermediate" in user_message:
            response = workouts["intermediate"]
        elif "advanced" in user_message:
            response = workouts["advanced"]
        else:
            response = "Please specify your level: beginner, intermediate, or advanced."
    elif "track" in user_message:
        response = "Tracking feature coming soon! Stay tuned."
    elif "help" in user_message:
        response = "I can suggest workouts. Try typing 'beginner workout' or 'advanced workout'."
    else:
        response = "I'm sorry, I didn't understand that. Type 'help' for assistance."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
