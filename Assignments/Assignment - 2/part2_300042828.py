from typing import Union
from typing import Any
import sys

###
# Question 2.1
###

def seriesSum() -> Union[None, float]:
    """
        Returns the solution for (1000 + (1+(i^2))) for all 1 <= i <= n and where n is input by the user. If the user
        enters a negative n value, the function returns None.
    """
    answer = float(1000)
    n = int(input("Please enter a non-negative integer: "))

    if n < 0:
        return None
    if n == 0:
        answer = 1000
        return answer
    else:
        for i in range(1, (n+1)):
            answer += float(1/(i**2))
        return answer

###
# Question 2.2
###

def catch(side: float, x: float, y: float) -> Union[None, tuple]:
    """
        Returns none if side value is invalid (less than or equal to 0).
        Returns the bottom left x,y coordinates as a tuple for the box so that the given x,y falls right in the middle
        of the box. The returned coordinates are calculated by subtracting half of the side value from the given x,y.
    """
    if side <= 0:
        return None
    else:
        return float(x- (side / 2)), float(y - (side / 2))

###
# Question 2.3
###

def pell(n: int) -> Union[None, int]:
    """
        Returns the n'th term in the Pell series. If n < 0, returns None.
    """

    pell_arr = [0, 1]

    if n < 0:
        return None
    else:
        for i in range(2, n+1):
            value = int(2 * pell_arr[i-1] + pell_arr[i - 2])
            pell_arr.append(value)

    return pell_arr[n]

print(pell(5))

###
# Question 2.4
###

def countMembers(s: str) -> int:
    """
        Returns the number of extraordinary characters in the given string.
    """
    extraordinary = ["e", "f", "g", "h", "i", "j", "Q", "R", "S", "T", "U", "V", "W", "X", "2", "3", "4", "5", "6", "!", ",", "\\"]

    answer = 0

    listified = list(s)

    for i in listified:
        answer += extraordinary.count(i)

    return answer

###
# Question 2.5
###

def encrypt(s: str) -> str:
    """
        Returns an encrypted version of s as a string.
    """

    return "".join(s[len(s)-1-i]+s[i] for i in range(len(s)))[:len(s)]

###
# Question 2.6
###

def alienNumbers(s: str) -> int:
    """
        Returns the alien numeric value for the given string s.
    """

    return 1024 * s.count("T") + 598 * s.count("y") + 121 * s.count("!") + 42 * s.count("a") + 6 * s.count("N") + 1 * s.count("U")

###
# Question 2.7
###

def alienNumbersAgain(s: str) -> int:
    """
        Returns the alien numeric value for the given string s without using string methods.
    """

    # Did it in one line, sorry its so long.

    return sum(1024 if i == "T" else (598 if i == "y" else (121 if i == "!" else (42 if i == "a" else (6 if i == "N" else (1 if i == "U" else 0))))) for i in s)

###
# Question 2.8
###

def oPify(s: str) -> str:
    """
        Returns a string according to the oPify conditions and rules.
    """
    listified = list(s)
    ans = []

    # Loop through the indexes of listified string, but stop at the second last letter
    for i in range(0, len(listified) - 1):

        if listified[i].isalpha() and listified[i+1].isalpha():

            if listified[i].isupper():
                # If the i index letter in listified is capital, add the i index letter to answer and a capital O.
                ans.append(listified[i])
                ans.append("O")

            else:
                # Similar to above if statement, but for lowercase o.
                ans.append(listified[i])
                ans.append("o")

            if listified[i+1].isupper():
                # If the i+1 index letter in listified is capital, add the capital letter P. Note we do not add the i+1
                # index letter itself (that will happen in the next iteration when i = i+1)
                ans.append("P")

            else:
                # Similar to above if statement, but for lowercase p.
                ans.append("p")

        else:
            # If either the i index or
            ans.append(listified[i])

    ans.append(listified[len(listified) - 1])

    ans_str = ""
    for i in ans:
        ans_str += i

    return ans_str

###
# Question 2.8
###

def battleOutcome(s: str) -> str:
    """
        Returns the battle outcome.
    """
    list_of_colors = s.lower().split()

    count_red = list_of_colors.count("red")
    count_green = list_of_colors.count("green")
    count_blue = list_of_colors.count("blue")

    power_red = count_red
    power_green = count_green
    power_blue = count_blue * 1.5

    if power_blue >= (power_red * 2):
        return "The Jedi army destroys the Sith army."
    elif power_blue >= (power_red * 1.5):
        return "The Jedi army defeats the Sith army."
    elif power_blue < (power_red * 1.5) and (power_blue * 1.5) > power_red:
        return "Ooh! This is going to be interesting."
    elif (power_blue * 2) <= power_red:
        return "The Sith army destroys the Jedi army."
    elif (power_blue * 1.5) <= power_red:
        return "The Sith army defeats the Jedi army."

def battleInterface():
    """
        Prompts the Jedi High Council to enter a space separated string for battleOutcome.
    """
    s = input("Please enter a space separated string of the 3 light saber colours: ")
    print("This is what’s going to happen: " + battleOutcome(s))

###
# BONUS CHALLENGE
# Question 3.1
###

# This function is here to test callfunc
def sum3(a,b,c):
    return a+b+c

def callfunc(func, args: tuple) -> Any:
    """
    (function, tuple) -> any type

    Receives function named called func which takes 3 parameters. Args is received a tuple of length 3 (which are the
    parameters for func.

    Returns the value upon calling func(args[0], args[1], args[2]). Return could be of any type.
    """
    return func(args[0], args[1], args[2])
