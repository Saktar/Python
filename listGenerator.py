#imports the ability to get a random number (we will learn more about this later!)
from random import *

#MENU GENERATOR

#Create the list of words you want to choose from.
aList = [0, 1]
sides = ["fries", "salad", "fruit"]
courses = ["steak", "hamburger", "rice with chicken"]
desserts = ["cake", "pudding", "macaroons"]
drinks = ["coke", "water", "smootie"]

#Generates a random integer.
aRandomIndex = randint(0, len(sides)-1)
print("You will eat a", sides[aRandomIndex])

aRandomIndex = randint(0, len(courses)-1)
print("You will eat a", courses[aRandomIndex])

aRandomIndex = randint(0, len(desserts)-1)
print("You will eat a", sides[aRandomIndex])

aRandomIndex = randint(0, len(drinks)-1)
print("You will drink a", drinks[aRandomIndex])

#HAIKU GENERATOR

aList = [0, 1]
syllable = ["You are strong", "Reach the stars", "Keep on trying"]
phrase = ["You will get back up", "You will reach my goals", "No one can stop you"]

aRandomIndex = randint(0, len(syllable)-1)
print(syllable[aRandomIndex])

aRandomIndex = randint(0, len(phrase)-1)
print(phrase[aRandomIndex])
