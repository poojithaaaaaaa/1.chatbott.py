import re
def chatbot_response(user_input):
    user_input = user_input.lower()
    if re.search(r'\bhello\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a bot, but I'm here to help you!"
    elif re.search(r'\bwhat is your name\b', user_input):
        return "I am a simple rule-based chatbot."
    elif re.search(r'\bbye\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\bhelp\b', user_input):
        return "Sure! I'm here to help you. Ask me anything."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Chatbot: Hi! I'm a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    main()
