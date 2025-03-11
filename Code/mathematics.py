import math

def is_prime(n: int) -> bool:
    '''
    Check if a number is prime.
    
    Args:
        n: A positive integer to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Raises:
        ValueError: If input is not a positive integer
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    '''

    # Input validation
    if not isinstance(n, int):
        raise ValueError('Input must be an integer')
    if n <= 1:
        return False
    
    # Check if n is 2 or 3
    if n <= 3:
        return True
    
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check numbers up to square root of n
    # Only need to check numbers of form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def quadratic_formula(a: float | int, b: float | int, c: float | int) -> tuple[float | int] | None: 
    '''
    Solve quadratic equation using the quadratic formula.
    
    Args:
        a: Coefficient of x², must be non-zero
        b: Coefficient of x
        c: Constant term
        
    Returns:
        tuple[float | int]: Tuple of roots (returns integers if roots are whole numbers)
        None: If no real roots exist
        
    Raises:
        ValueError: If a is zero
        TypeError: If inputs are not numbers
        
    Examples:
        >>> quadratic_formula(1, 5, 6)    # x² + 5x + 6 = 0
        (-2, -3)                          # integer roots
        >>> quadratic_formula(1, -2, 1)   # x² - 2x + 1 = 0
        (1, 1)                            # integer roots
        >>> quadratic_formula(2, -7, 3)   # 2x² - 7x + 3 = 0
        (3, 0.5)                        # float roots
        >>> quadratic_formula(1, 0, 1)    # x² + 1 = 0
        None                              # no real roots
    '''

    def to_int_if_whole(x: float) -> float | int:
        '''Convert float to int if it's a whole number'''
        return int(x) if abs(x - round(x)) < 1e-10 else x

    # Input validation
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError('All coefficients must be numbers')
    if abs(a) < 1e-10:
        raise ValueError('Coefficient "a" cannot be zero')

    # Calculate discriminant
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return None

    two_a = 2 * a
    neg_b = -b

    # Handle perfect square discriminant for integer inputs
    if all(isinstance(x, int) for x in (a, b, c)):
        root = math.isqrt(discriminant) if math.isqrt(discriminant) ** 2 == discriminant else math.sqrt(discriminant)
        x1 = (neg_b + root) / two_a
        x2 = (neg_b - root) / two_a
        return (to_int_if_whole(x1), to_int_if_whole(x2))

    # Handle near-zero discriminant
    if abs(discriminant) < 1e-10:
        x = neg_b / two_a
        return (to_int_if_whole(x), to_int_if_whole(x))

    # Regular case
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (neg_b + sqrt_discriminant) / two_a
    x2 = (neg_b - sqrt_discriminant) / two_a
    return (to_int_if_whole(x1), to_int_if_whole(x2))

def continued_ratio(coefficient: tuple[float | int]) -> tuple[int]:
    '''
    Calculate the continued ratio for given coefficients.
    
    Args:
        coefficient: A tuple of 3 numbers (a, b, c) representing ax + by + cz
        
    Returns:
        A tuple of 3 integers representing the simplified ratio x:y:z
        
    Example:
        >>> continued_ratio((3, 4, 4))  # 3x + 4y + 4z
        (4, 3, 3)  # x : y : z = 4 : 3 : 3
        >>> continued_ratio((2.5, 5, 7.5))
        (6, 3, 2)  # handles floating point numbers
        
    Raises:
        ValueError: If coefficient tuple doesn't have exactly 3 elements
        ValueError: If any coefficient is zero
        ValueError: If any coefficient is not a number
    '''

    # Validate input length
    if len(coefficient) != 3:
        raise ValueError('Coefficient tuple must contain exactly 3 elements')
    
    # Convert to float for validation
    try:
        a, b, c = map(float, coefficient)
    except (TypeError, ValueError):
        raise ValueError('All coefficients must be numbers')
    
    # Check for zeros
    if any(abs(x) < 1e-10 for x in (a, b, c)):
        raise ValueError('Coefficients cannot be zero or very close to zero')
    
    # Convert to integers by finding LCM of denominators
    def to_fraction(x):
        from fractions import Fraction
        return Fraction(x).limit_denominator()
    
    fa, fb, fc = map(to_fraction, (a, b, c))
    lcm = math.lcm(fa.denominator, fb.denominator, fc.denominator)
    
    # Calculate final values
    a_int = int(a * lcm)
    b_int = int(b * lcm)
    c_int = int(c * lcm)
    
    # Calculate ratios
    x = b_int * c_int
    y = a_int * c_int
    z = a_int * b_int
    
    # Find GCD and simplify
    gcd = math.gcd(math.gcd(abs(x), abs(y)), abs(z))
    
    return (x // gcd, y // gcd, z // gcd)
