import os
import sys


def stringSimilarity(inputs):
    results = []
    i = 0
    while i < len(inputs):
        word = inputs[i]
        arr = get_strings(word)
        counter = 0
        score = []
        while counter < len(arr):
            counter1 = 0
            word_versus = word[counter:]
            score.append(0)
            while word[counter1] == word_versus[counter1]:
                score[counter] += 1
                if counter1 < len(word_versus) - 1:
                    counter1 += 1
                else:
                    break
            counter += 1
        results.append(sum_scores(score))
        i += 1

    return results


def get_strings(s):
    counter = 0
    arr_of_strings = []
    while counter < len(s):
        arr_of_strings.append(s[counter:])
        counter += 1

    return arr_of_strings

def sum_scores (scores):
    sum = 0
    counter = 0

    while counter < len(scores):
        sum += scores[counter]
        counter += 1

    return sum

print(stringSimilarity(["ababaaabbabbabbbabbababbabbbbababbbababbbabababbabaaabbbabbabaabbababababbabababbabababbabababbbbabbaaaaabbabab"]))