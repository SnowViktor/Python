def angle_to_runway_number(angle: int | str) -> str:
    """
    Convert a magnetic heading angle to a standard runway number.

    Args:
        angle (int | str): The magnetic heading in degrees. Can be an integer or a string (optionally ending with "°").

    Returns:
        str: The runway number as a two-digit string ("01" to "36").

    Examples:
        >>> angle_to_runway_number(0)
        "36"
        >>> angle_to_runway_number(45)
        "05"
        >>> angle_to_runway_number("270°")
        "27"
    """
    if isinstance(angle, str):
        angle = angle.rstrip("°")

    angle = int(angle) % 360
    runway_num = (angle + 5) // 10 % 36

    return f"{runway_num:02d}" if runway_num != 0 else "36"


if __name__ == "__main__":
    angle = input("\n請輸入角度：")
    print(f"跑道編號：{angle_to_runway_number(angle)}")
