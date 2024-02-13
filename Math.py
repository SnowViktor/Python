import math

def QuadraticFormula(a: float | int, b: float | int, c: float | int) -> float | str | None: 
    '''
    QuadraticEquation: ax² + bx + c = 0 (a ≠ 0)

    QuadraticFormula: (-b ± √(b²-4ac)) / (2a)

    Discriminant: b² - 4ac
        < 0 -> None

        = 0 -> float

        > 0 -> str,str
    '''
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x = None # No Real Roots
    elif discriminant == 0:
        x = -b / 2 * a
    elif discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        x = str(x1) + ',' + str(x2)
    return x

def IsPrime(positive_integer: int) -> bool:
    for i in range(2, positive_integer):
        if positive_integer % i == 0:
            return False
    return True