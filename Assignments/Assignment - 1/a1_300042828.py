# Name: Harsh Gupta
# Student number: 300042828
# E-mail: hgupt033@uottawa.ca or me@harshgupta.ca
# Course: IT1 1120
# Section C
# Assignment No. 1

from typing import Union
import math
import turtle


########################
# Question 1
########################

def mh2kh(s: Union[int, float]) -> Union[int, float]:
    """
         Converts the given speed from miles per hour to kilometres per hour and returns it
    """
    conversionFactor = 1.60934

    kh = s * conversionFactor

    return kh


########################
# Question 2
########################

def pythagorean_pair(a: int, b: int) -> bool:
    """
         Determines whether a and b are pythagorean pairs on the basis that c^2 = a^2 + b^2 and c is an integer.
         If c is not an integer, false. If it is, true.
    """
    c = math.sqrt(a ** 2 + b ** 2)

    checker = (c == int(c))

    return checker


########################
# Question 3
########################

def in_out(xs: Union[int, float], ys: Union[int, float], side: Union[int, float]):
    """
         Returns bool for whether a user input coordinate falls within the square defined by the parameters
         given to the function (coordinate of bottom left corner and side lengths)
    """
    xUser = float(input("Enter the x coordinate: "))
    yUser = float(input("Enter the y coordinate: "))

    # Check whether the user input x coordinate is to the right of the left side of the square and to the left of the
    # right side of the square
    checkX = ((xs <= xUser) & (xUser <= (xs + side)))
    # Check whether the user input y coordinate is above the bottom side of the square and below the
    # top side of the square
    checkY = ((ys <= yUser) & (yUser <= (ys + side)))

    # The question asks that the true or false be printed
    print(checkX & checkY)


########################
# Question 4
########################

def safe(n: int) -> bool:
    """
        Determines whether given number n is divisible by 9 or contains 9 as a digit. If any of the
        conditions are true, this function returns false. Else, true.
    """
    # isolate ones digit
    ones = n % 10
    # isolate tens digit
    tens = int((n - ones) / 10)

    # checks to make sure whether n is not divisible by 9 and does not contain 9 as a digit
    return (n % 9 != 0) & (ones != 9) & (tens != 9)

########################
# Question 5
########################

def quote_maker(quote: str, name: str, year: Union[int, str]) -> str:
    """
        Concatenates strings into a cohesive sentence such as: "In [year], a person called [name] said: [quote]"
    """
    return "In " + str(year) + ", a person called " + str(name) + " said: \"" + str(quote) + "\""


########################
# Question 6
########################

def quote_displayer():
    """
        Asks user for input for quote, name and year and feeds that to quote_maker function above.
        Prints the outcoming sentence.
    """
    quote = input("Please enter a quote: ")
    name = input("Who said this quote? ")
    year = input("When did this person say this quote? ")

    print(quote_maker(quote, name, year))


########################
# Question 7
########################

def rps_winner():
    """
        Takes two inputs, for player1 and player2 respectively, that is rock, paper or scissors in string type.
        Prints whether player 1 won or not. Prints whether it is a tie or not.
    """
    player1 = input("What choice did player 1 make?\nType one of the following options - rock, paper or scissors: ")
    player2 = input("What choice did player 2 make?\nType one of the following options - rock, paper or scissors: ")

    print("Player 1 wins. That is " + str((((player1 == "rock") & (player2 == "scissors")) |
                                           ((player1 == "scissors") & (player2 == "paper")) |
                                           ((player1 == "paper") & (player2 == "rock"))
                                           )) +".")
    print("It is a tie. That is not " + str(not (player1 == player2)) + ".")

########################
# Question 8
########################

def fun(x: Union[int, float]) -> float:
    """
        Calculates y in the equation 10^(4y) = x + 3 and returns it.
    """
    return math.log(x + 3, 10) / 4


########################
# Question 9
########################

def ascii_name_plaque(name: str):
    """
        Prints a name plaque.
    """
    nameLength = len(name)

    print("*****" + ("*" * nameLength) + "*****")
    print("*    " + (" " * nameLength) + "    *")
    print("*  __" + name + "__  *")
    print("*    " + (" " * nameLength) + "    *")
    print("*****" + ("*" * nameLength) + "*****")


########################
# Question 10
########################

def my_fun_drawing():
    """
        Draws a flower using the turtle module.
    """
    s = turtle.Screen()
    t = turtle.Turtle()

    t.pensize(3)

    t.color("red")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(50)
            t.left(90)
        t.left(36)
    t.left(18)
    t.color("green")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(50)
            t.left(90)
        t.left(36)
    t.left(18)

    t.pensize(1)

    t.color("blue")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(100)
            t.left(90)
        t.left(36)
    t.left(18)
    t.color("yellow")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(100)
            t.left(90)
        t.left(36)
    t.left(18)
    t.color("orange")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(150)
            t.left(90)
        t.left(36)
    t.left(18)
    t.color("cyan")
    for outer in range(10):  # repeat 10 times
        for inner in range(4):  # repeat four times
            t.forward(150)
            t.left(90)
        t.left(36)
    t.left(18)
    t.pensize(3)
    t.color("purple")
    for outer in range(10):  # repeat 10 times
        for inner in range(2):  # repeat twice times
            t.forward(200)
            t.left(180)
        t.left(36)

########################
# Question 11
########################

def alogical (n: Union[int, float]) -> int:
    """
        Returns number of times a number, n must be divided by 2 for it to be equal to or less than 1.
    """

    # Question boils down to n/(2^x) = 1, solve for x and then round up to nearest int

    # math.log will give a float value, math.ceil will round up, int will make sure the value is int type (redundantly)
    return int(math.ceil(math.log(n, 2)))

########################
# Question 12
########################

def time_format(h: int, m: int) -> str:
    """
        First the given minute (0 to 60) is rounded to the nearest 5 minute interval.
        Returns a readable time str for the given hour (0 to 24) and rounded minute (0 to 60).
    """
    mRounded = round((m)/5) * 5

    if (mRounded == 0):
        return str(h) + " o'clock"
    elif (mRounded < 30):
        return str(mRounded) + " past " + str(h) + " o'clock"
    elif (mRounded == 30):
        return "Half past " + str(h) + " o'clock"
    elif ((mRounded > 30) & (mRounded < 60)):
        return str(60 - mRounded) + " minutes to " + str(h + 1) + " o'clock"
    elif (mRounded == 60):
        return str(h + 1) + " o'clock"

    if h == 23 and (60 > mRounded > 30):
        return str(60 - mRounded) + " minutes to " + str(0) + " o'clock"
    elif h == 23 and (mRounded == 60):
        return str(0) + "o'clock"

########################
# Question 13
########################

def cad_cashier(price: Union[int, float], payment: Union[int, float]) -> float:
    """
        Rounds the price to nearest 0.05 cents.
        Returns change due, where change = payment minus the rounded price
    """
    # Rounding to nearest 0.05
    priceRounded = round(price / 0.05) * 0.05

    # Round to two decimal places, float subtraction isn't exactly straightforward.
    return round((payment - priceRounded), 2)

########################
# Question 14
########################

def min_CAD_coins(price: Union[int, float], payment: Union[int, float]) -> tuple:
    """
        Returns minimum number of each type of coins that need to be given for the change in a list type variable.
    """

    # Calculate cents to be returned
    cents = round(cad_cashier(price, payment) * 100, 0)

    # cents // 200 gives the number of toonies that can be given
    # cents % 200 gives the remaining change to be calculated after toonies.
    t = int(cents // 200)
    cents = cents % 200
    # Repeat above two lines for loonies, quarters, dimes and nickels.
    l = int(cents // 100)
    cents = cents % 100

    q = int(cents // 25)
    cents = cents % 25

    d = int(cents // 10)
    cents = cents % 10

    n = int(cents // 5)
    cents = cents % 5

    return t, l, q, d, n
