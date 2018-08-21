
def digit_sum(n: int) -> int:
    """
    Calculates the sum of all the digits of n
    :param n: a positive integer
    :return: sum of all the digits of n
    """

    if n // 10 == 0:
        return n

    return int((n % 10) + digit_sum(n // 10))

def digital_root(n: int) -> int:
    """
    Calculates the digital root of n.
    :param n: a positive integer
    :return: returns an int for the digital root of the number n.
    """

    s = digit_sum(n)

    if s // 10 != 0:
        s = digital_root(s)

    return s



