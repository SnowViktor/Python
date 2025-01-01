import math

def is_prime(positive_integer: int) -> bool:
    for i in range(2, positive_integer):
        if positive_integer % i == 0:
            return False
    return True

def quadratic_formula(a: float | int, b: float | int, c: float | int) -> list[float] | None: 
    '''
    Quadratic Equation: ax² + bx + c = 0 (a ≠ 0)

    Quadratic Formula: (-b ± √( b² - 4ac )) / 2a

    Discriminant: b² - 4ac
    '''

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None # No Real Roots
    elif discriminant == 0:
        x = (-b) / (2 * a)
        return [x, x] # One Real Root (repeated)
    elif discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant)  / (2 * a)
        return [x1, x2] # Two Real Roots
    else:
        pass