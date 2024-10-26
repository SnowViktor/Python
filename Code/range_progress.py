from math import floor

def range_progress(variable: int, start: int, stop: int, step: int = 0) -> str:
    '''
    ### Remember to add , end='\\r'

    Example:
    
        >>> for i in range(2, 100):
        >>>     # variable = i, start = 2, stop = 100, step = 0
        >>>     print(range_progress(i, 2, 100), end='\\r')
    '''
    
    BAR_TOTAL = 25
    total = stop - start
    variable = variable - start + 1 + step

    # Limit progress to 100% when variable exceeds total
    progress_percentage = min(100, round(variable * 100 / total))
    progress_bar = min(BAR_TOTAL, floor(variable * BAR_TOTAL / total))

    return f' [{"▮" * progress_bar}{"▯" * (BAR_TOTAL - progress_bar)}] {progress_percentage}%'

if __name__ == '__main__':
    from time import sleep

    start = 2
    stop = 100
    step = 0
    total_duration = 5
    iterations = stop - start
    delay = total_duration / iterations

    for i in range(start, stop):
        print(range_progress(i, start, stop, step), end='\r')
        sleep(delay)