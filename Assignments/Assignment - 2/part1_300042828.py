import math
from random import randint


def performTest(flag: int, n: int) -> int:
    """
    Based on flag (0 or 1), the function prompts the user for n number of questions for either subtraction or
    exponentiation and returns how many questions the user answered correctly.
    """
    correctCounter = 0
    if flag == 0:
        # subtraction

        correctCounter = 0

        for i in range(n):
            num1 = int(randint(1, 9))
            num2 = int(randint(1, 9))

            userAnswer = int(input("What is " + str(num1) + " - " + str(num2) + "? ").strip())

            if userAnswer == (num1 - num2):
                correctCounter += 1
    elif flag == 1:
        # exponentiation

        correctCounter = 0

        for i in range(n):
            num1 = int(randint(0, 9))
            num2 = int(randint(0, 9))

            userAnswer = int(input("What is " + str(num1) + " ^ " + str(num2) + "? ").strip())

            if userAnswer == (num1 ** num2):
                correctCounter += 1

    return correctCounter

print(performTest(0,1))

if __name__ == "__main__":
    # your code goes here
    name = input("Hi! What's your name? ").strip()
    flag = input("What would you like to practice? \n 0: subtraction \n 1: exponentiation - ").strip()
    n = int(input("How many questions would you like to work on? ").strip())

    if n != 0:
        performance = round(float(performTest(int(flag), n) / n), 2)

        if performance >= 0.90:
            print("Congratulations " + name + "! You'll probably get an A tomorrow. \nNow go eat your dinner and go to sleep. Good bye " + name + "!")
        elif performance >= 0.70:
            print("You did well " + name + ", but I know you can do better. \nGood bye " + name + "!")
        else:
            print("I think you need more practice " + name + ". \nGood bye " + name + "!")

# your code goes here
