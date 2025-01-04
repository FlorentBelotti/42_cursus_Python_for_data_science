def ft_tqdm(lst: range):

    """
    Custom implementation of tqdm using yield to create a generator.

    :param lst: A range object to iterate over.
    :return: A generator that yields elements from lst
    while displaying a progress bar.
    """

    total = len(lst)
    progress = 0
    bar_len = 127

    for item in lst:
        progress += 1
        perc = (progress / total) * 100
        filled = int(bar_len * progress // total)
        bar = '=' * (filled - 1) + '>' + ' ' * (bar_len - filled) + ']'
        print(f'\r{perc:.0f}%|[{bar}| {progress}/{total}', end='\r')
        yield item
    print()
