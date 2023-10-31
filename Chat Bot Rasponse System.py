from urllib import response


def get_response(user_input):
    responses = {
       "hello": "Hello! How can I help you?",
       "how are you": "I'm just a chatbot, but I'm here to assist you",
       "what's your name": "I'm a chatbot. You can call me Chatbot.",
       "bye": "Goodbye! Have a great day!",
    }

    user_input = user_input.lower()

    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that."
    
def main():
    print("Chatbot: Hi there! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    main()