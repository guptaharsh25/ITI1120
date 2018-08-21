# Q 1a
def largest_34(a: list) -> int:
    """
    :param a: A list of distinct integers
    :return: Returns the sum of the third and fourth largest numbers in this list.
    """

    a.sort()  # O(nlogn)

    return a[-3] + a[-4]  # O(1)
    # O(nlogn + 1)

# Q 1b
def largest_third(a: list) -> int:
    """
    :param a:  A list of distinct integers
    :return: Sum of the largest third of the list.
    """

    a.sort(reverse=True)  # O(nlogn)

    index_largest3 = len(a)//3  # O(1)

    return sum(i for i in a[:index_largest3])  # O(n//3)

print(largest_third( [12.2, 3.14, -2.77, 0, -67] ))

# Q 1c
def third_at_least(a: list) -> int:
    """
    :param a:  A list of integers of length 4 or greater.
    :return: A number that occurs is param a at least len(a)//3 + 1 times.
    """

    count = len(a) // 3 + 1  # O(1)

    a.sort()  # O(nlogn)

    for i in range(count-1, len(a)):  # O(n)
        if a[i-count+1:i+1] == [a[i]] * count:
            return a[i]

# Q 1d
def sum_tri(a: list, x: int) -> bool:
    """
    :param a: a list of integers
    :param x: an integer
    :return: whether there exists a combination of 3 numbers in a which sums to x.
    """

    #a.sort(reverse=True)

    for i in a:
        for j in a:
            for k in a:
                if i+j+k == x:
                    return True
