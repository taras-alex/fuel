def fuel(expense, stock):
    """
    >>> fuel(10,100)
    900.0

    """
    resere = 0.1
    result = (1 - resere) * (stock / expense) * 100
    return result
