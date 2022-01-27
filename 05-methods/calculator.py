
def calculate(x: int, y: int = 1, *, subtract: bool = False) -> int:
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int, required
        The first number
    `y` : int, optional
        The second number (default is 1)
    `subtraction`: bool, optional
        Whether to perform subtraction. Default is False.
    """

    return x - y if subtract else x + y


author = "Hugh Lilly"
