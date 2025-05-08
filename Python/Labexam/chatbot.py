import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm good!", "Doing well, thanks!", "All good here."],
    "what is your name": ["I'm ChatBot!", "Just call me Bot."],
    "bye": ["Goodbye!", "See you!", "Bye!"],
    "myre": ["poyioomb!", "kootichi mone!", "pundachi mone!"],
    "default": ["I didn't get that.", "Could you rephrase?", "Tell me more."]
}

def get_response(text):
    text = text.lower()
    for key in responses:
        if key in text:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def chatbot():
    print("ChatBot: Hi! Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("ChatBot: Bye!")
            break
        print("ChatBot:", get_response(msg))

chatbot()



