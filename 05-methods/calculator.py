
def calculate(x: int, y: int, *, subtraction: bool = False) -> int:
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int
        The first number
    `y` : int, optional
        The second number (default is 1)
    `subtraction`: bool, optional
        Whether to perform subtraction. Default is False.
    """

    if subtraction:
        return x - y
    return x + y


author = "Hugh Lilly"
