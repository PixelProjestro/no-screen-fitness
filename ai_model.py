def generate_response(user_message):
    """Generate a simple response for non-workout queries."""
    if "help" in user_message.lower():
        return "I can suggest workouts or track your progress. Type 'beginner workout' to get started!"
    return "I'm sorry, I didn't understand that. Try typing 'help'."
