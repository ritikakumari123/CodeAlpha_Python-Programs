# Simple Rule-Based Chatbot (Improved Version)

def chatbot():
    print("Chatbot Activated!")
    print("You can chat with me now ")
    print("Try: hello, hi, how are you, your name, help, time, bye\n")

    while True:
        user_input = input("You: ").lower()

        # greetings
        if user_input in ["hello", "hi", "hey"]:
            print(" Chatbot: Hello! Nice to meet you ")

        # how are you
        elif user_input in ["how are you", "how r you", "how are you doing"]:
            print(" Chatbot: I'm doing great! Thanks for asking ")

        # name related
        elif user_input in ["what is your name", "your name", "who are you"]:
            print(" Chatbot: I'm a simple Python chatbot created by Ritika ")

        # help option
        elif user_input in ["help", "what can you do"]:
            print(" Chatbot: I can respond to greetings, tell my name, and say goodbye.")

        # time response (basic static reply)
        elif user_input in ["time", "what is the time"]:
            print(" Chatbot: Sorry, I cannot show real-time clock yet ")

        # goodbye
        elif user_input in ["bye", "exit", "quit"]:
            print(" Chatbot: Goodbye! Have a great day ")
            break

        # empty input
        elif user_input == "":
            print(" Chatbot: Please type something...")

        # default response
        else:
            print("Chatbot: Sorry, I don't understand that yet. Try 'help'.")

# run chatbot
chatbot()
