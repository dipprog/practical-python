# timethis.py

def timethis(func):
    '''
    Decorator function that prints out how long it takes for a
    function to execute.
    '''
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))

    return wrapper
