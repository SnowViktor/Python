def runway(degree: int | str) -> str:
    '''
    Convert an angle to a runway number.

    Args:
        degree (int | str): The angle in degrees, can be an integer or a string (with or without '°').

    Returns:
        str: The runway number as a two-digit string.

    Examples:
        >>> runway(0)
        '36'
        >>> runway(45)
        '05'
        >>> runway('270°')
        '27'
    '''

    if isinstance(degree, str):
        degree = degree.rstrip('°')
    degree = int(degree) % 360
    
    runway_num = (degree + 5) // 10 % 36
    return f"{runway_num:02d}" if runway_num != 0 else "36"