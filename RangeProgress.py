from math import floor

def range_progress(variable: int, start: int, stop: int, step: int = 0) -> str:
    '''
    ## Remember to add , end='\\r'    
    Example↓\n
    for i in range(2, 100):\n
        # variable = i, start = 2, stop = 100, step = 0\n
        print(range_progress(i, 2, 100), end='\\r')
    '''

    BAR_TOTAL = 25
    variable = variable - start + 1
    total = stop - start

    if variable + step >= total:
        progress_bar = BAR_TOTAL
        progress_percentage = 100
    else:
        progress_bar = floor(variable * (BAR_TOTAL / total))
        progress_percentage = round(variable * (100 / total))

    progress = f' [{'▮' * progress_bar}{'▯' * (BAR_TOTAL - progress_bar)}] {progress_percentage}%'
    return progress