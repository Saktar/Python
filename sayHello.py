#Global variables
# def say_hello():
#     print("Hi" + name)
#
# name = "Michelle"
# say_hello()

# #Local variable
# def say_hello():
#     print("Hi" + name)
#
# def main():
#     name = "Michelle"
#     say_hello()
#
# if _name_ == "_main_":
#     main()
# we got NameErrors

#Parameter
# def say_hello(name):
#     print("Hi " + name)
#
# def main():
#     user = "Michelle"
#     say_hello(user)
#
# if __name__ == "__main__":
#     main()

#Return value
# def add(num1, num2):
#     sum = num1 + num2
#     return sum

#Alternative Return value
# def add(num1, num2):
#     return num1 + num2

# def add(num1, num2):
#     sum = num1 + num2
#     return sum
#     print(sum)

#Adding list
# def calc_total():
#     num = [1, 2, 3, 4]
#     total = sum(num)
#     print(total)
#
# def main():
#     calc_total()
#
# if __name__ == "__main__":
#   main()

#Calclating Sum
def calc_total(list):
    total = 0
    #loop
    for item in list:
        total+= item
    print(total)
    return total

def main():
    scores = [100, 99, 80, 78, 60, 40, 100, 35, 90]
    calc_total(scores)

if __name__ == "__main__":
  main()

#Determine whether number is even or not
def is_even(num):
    if num%2 == 0:
        print("True")
        return True
    else:
        print("False")
        return False

def main():
    number = int(input("Please enter a number."))
    is_even(number)

if __name__ == "__main__":
  main()
