def getScore(s):


def getPalin1(s):
    counter = 0
    word = ""

    while counter < len(s):
        letter = s[counter]
        pos_of_letter = []
        #word = s[counter] + s[counter+1]
        counter1 = 1

        # gives us every position that letter recurs at
        while counter1 < len(s):
            if s[counter1] == letter:
                pos_of_letter.append(counter1)
            counter1 += 1

        strings = []
        strings

        counter += 1