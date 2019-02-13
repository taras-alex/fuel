def fuel(expense, stock):
    """
    >>> fuel(10,100)
    900.0

    """
    reserve = 0.1
    result = (1 - reserve) * (stock / expense) * 100
    return result
