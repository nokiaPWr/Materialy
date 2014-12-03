def multiply_string(s, n, sep=' '):
    '''
    Docstring
    >>> multiply_string('a', 2)
    'a a'
    >>> multiply_string('b', 0)
    Traceback (most recent call last):
    ...
    ValueError: n should be greater than 0
    '''
    if n <= 0:
        raise ValueError('n should be greater than 0')
    return sep.join([s] * n)


#python -m doctest *nazwaskryptu*
