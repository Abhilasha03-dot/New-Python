def chatbot_response(user_input):
    user_input = user_input.lower()  # convert to lowercase for easy matching

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "how are you":
        return "I'm fine, thanks! How can I help you today?"
    elif user_input == "what is your name":
        return "I'm ChatBot, your virtual assistant."
    elif user_input == "bye":
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand that."

def run_chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("🤖 ChatBot:", response)
        if user_input.lower() == "bye":
            break

# Start the chatbot
run_chatbot()
