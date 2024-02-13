def RangeProgress(variable: int, start: int, stop: int, step: int = 0) -> str:
    '''
    Example:

    for i in range(2, 100):
    
        # variable = i, start = 2, stop = 100, step = 0
    
        print(RangeProgress(i, 2, 100))

    Remember to add , end='\\r'
    '''
    variable = variable - start + 1
    total = stop - start
    bar_total = 25
    percentage = 100
    bar_conversion = bar_total / total
    percentage_conversion = percentage / total

    if variable + step >= total:
        progress_bar = bar_total
        progress_percentage = percentage
    else:
        progress_bar = round(variable * bar_conversion)
        progress_percentage = round(variable * percentage_conversion)
    
    progress = '[' + str('▮' * progress_bar) + str('▯' * (bar_total - progress_bar)) + '] ' + str(progress_percentage) + '%'
    return progress