def factorial(n):
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n == 0 or n == 1:
        return 1
    else:
        return  n * factorial(n-1)
