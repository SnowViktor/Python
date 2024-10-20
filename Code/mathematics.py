from math import sqrt as _sqrt

def is_prime(positive_integer: int) -> bool:
    for i in range(2, positive_integer):
        if positive_integer % i == 0:
            return False
    return True

def quadratic_formula(a: float | int, b: float | int, c: float | int) -> list[float] | None: 
    '''
    ### Quadratic Equation: ax² + bx + c = 0 (a ≠ 0)\n
    ### Quadratic Formula: (-b ± √(b²-4ac)) / (2a)\n
    Discriminant: b² - 4ac
        < 0 -> None\n
        = 0 -> list\n
        > 0 -> list
    '''

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x = None # No Real Roots
    elif discriminant == 0:
        x1 = -b / (2 * a)
        x2 = -b / (2 * a)
        x = [x1, x2]
    elif discriminant > 0:
        x1 = (-b + _sqrt(discriminant)) / (2 * a)
        x2 = (-b - _sqrt(discriminant)) / (2 * a)
        x = [x1, x2]
    return x