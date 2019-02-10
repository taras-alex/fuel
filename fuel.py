def fuel(expense, stock):
    """
    >>> fuel(10,100)
    900.0

    """
    # k - magic numbers, запас хода +10%
    k = 0.9
    result = k * (stock / expense) * 100
    return result
