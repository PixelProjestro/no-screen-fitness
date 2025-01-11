import os

# Simulated database for demonstration
user_messages = []

workouts = {
    "beginner": ["10 push-ups", "15 squats", "20 jumping jacks"],
    "intermediate": ["20 push-ups", "25 squats", "30 jumping jacks"],
    "advanced": ["30 push-ups", "40 squats", "50 jumping jacks"],
}

def save_user_message(message):
    """Save user message to the database."""
    user_messages.append(message)

def get_workout_plan(message):
    """Retrieve a workout plan based on user input."""
    if "beginner" in message:
        return workouts["beginner"]
    elif "intermediate" in message:
        return workouts["intermediate"]
    elif "advanced" in message:
        return workouts["advanced"]
    else:
        return "Please specify your level: beginner, intermediate, or advanced."
