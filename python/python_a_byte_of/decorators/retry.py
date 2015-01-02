from time import sleep
from functools import wraps


def retry (f):
    """ Decorator which retries a wrapped function a number of times.

        Usage:
            @retry
            def fn():
                raise ValueError()

            fn()
    """

    @wraps(f)
    def wrapped_f (*args, **kwargs):

        MAX_ATEMPTS = 5
        for attempt in range(1, MAX_ATEMPTS+1):
            try:
                return f(*args, **kwargs)
            except:
                sleep(10 * attempt)

    return wrapped_f


class documenter(object):
    """ Adds documentation to a method if it does not already have it. """

    def __init__(self, *args):
        self.fn_doc = args[0]

    def __call__(self, fn):
        def decorated_function(*args):
            return fn(*args)

        if fn.__doc__:
            decorated_function.__doc__ = fn.__doc__ + ": " + self.fn_doc
        else:
            decorated_function.__doc__ = self.fn_doc
        return decorated_function
