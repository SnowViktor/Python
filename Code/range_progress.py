from math import floor

def range_progress(variable: int, start: int, stop: int, step: int = 0) -> str:
    '''
    Returns a progress bar string representing the progress of `variable` within the range from `start` to `stop`.

    Parameters:
    - variable (int): The current value within the range.
    - start (int): The starting value of the range.
    - stop (int): The ending value of the range.
    - step (int, optional): The step increment. Defaults to 0 if not provided.

    Example:
    
        >>> for i in range(2, 100):
        >>>     # variable = i, start = 2, stop = 100, step = 0
        >>>     print(range_progress(i, 2, 100), end='\\r')
    '''
    
    BAR_TOTAL = 25
    total = stop - start
    variable = variable - start + 1 + step

    progress_percentage = min(100, round(variable * 100 / total))
    progress_bar = min(BAR_TOTAL, floor(variable * BAR_TOTAL / total))

    return f' [{"▮" * progress_bar}{"▯" * (BAR_TOTAL - progress_bar)}] {progress_percentage}%'

if __name__ == '__main__':
    from time import sleep
    for i in range(2, 100):
        sleep(0.1)
        print(range_progress(i, 2, 100), end='\r')
