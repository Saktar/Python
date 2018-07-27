# Update this text to match your story.
start = '''
You wake up in a world full of talking animals and you find yourself turned into
an oranage cat. You find a map underneath your bed and realize it leads to
treasure.
'''

print(start)

print("Type 'forest' to go to the forest or 'cave' to go to the cave.")
user_input = input()
if user_input == "cave":
    print("You decide to go to the cave and you encounter a dragon in your path.")
    print("Type 'run' to run away or 'fight' to stay and fight the dragon.")
    user_input = input()
    if user_input == "run":
        print("You decide to run away and eventually escape the dragon. However by doing so you lose all respect people had for you.")
    if user_input == "stay":
        print("You turn into a knight and fight the dragon with a sword, however your die a miserable death from the dragon's fire breath.")
elif user_input == "forest":
    print("You choose to go to the forest and can't find the treasure anywhere.")

print("Type 'walk' to walk away or 'keep looking' to keep looking.")
user_input = input()
if user_input == "walk":
    print("You end up walking away from the greatest opportunity of your life and become very poor and lonely.")
if user_input == "keep looking":
    print(" You end up staying and looking around. You find the treasure hidden behind a bush.")

    # Continue code to finish story.
