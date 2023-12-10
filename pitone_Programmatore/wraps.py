from functools import wraps

def log_calls(func):
    fname = func.__name__
    @wraps(func)
    def logger(*args, **kwargs):
        print(fname, 'chiamata')
        return func(*args, **kwargs)
    return logger

@log_calls
def add(x, y):
    """Return the sum of x and y"""
    return x + y


print(add(1,1))
print(add.__doc__)
print(add.__module__)