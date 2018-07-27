# --- Define your functions below! ---

#The chatbot introduces itself and gives the user instructions
def intro():
    print("Hi, my name is Bot. Let's talk!")
    print("Type something and hit enter")

#The chatbot processes user user_input
def process_input(answer):
    # if(answer == "hi" or answer == "hello" or answer == "hey"):
    #     say_greeting()
    # else:
    #     say_default()

    #Alternative way of greeting
    greetings = ["hi", "hello", "hey", "yo", "hola", "howdy", "what's up", "sup"]
    if _is_valid_input(answer, greetings):
        say_greeting()
    else:
        say_default()

#Display a greeting message
def say_greeting():
    print("What's up?")

#Display a default message
def say_default():
    print("That's cool!")

#The chatbot continues the conversation
def next():
    print("Do you want to hear a poem?")
    print("Type yes or no")

def process_message(message):
    if(message == "yes" or message == "Yes"):
        say_poem()
    else:
        say_default()
#Display poem
def say_poem():
    print("All what-ifs and what can't be, I cast them out. Now I am free.")

#Check if user input matches one of the elements in valid responses
def _is_valid_input(user_input, valid_responses):
    for item in valid_responses:
        if user_input == item:
            #If you find a matching response, the input is valid
            return True
            #if it isn't true
    else:
            return False

#The chatbox continues the conversation
def then():
    print("Do you want to hear a joke?")
    print("Type yes or no")

def process_response(response):
    if(response == "yes" or response == "Yes"):
        say_joke()
    else:
        say_default()

def say_joke():
    print("What kind of music are balloons afraid of?.... Pop Music!!")

def end():
    print("I had alot of fun today. See you next time!")
    print("Bye!")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        #print("That's cool!")
        process_input(answer)
        break
    next()
    while True:
        message = input("(What will you say?) ")
        process_message(message)
        break
    then()
    while True:
        response = input("(What will you say?) ")
        process_response(response)
        break
    end()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
