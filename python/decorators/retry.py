from time import sleep
from functools import wraps


def retry (f):
    """ Decorator which retries a wrapped function a number of times. """

    @wraps(f)
    def wrapped_f (*args, **kwargs):

        MAX_ATEMPTS = 5
        for attempt in range(1, MAX_ATEMPTS+1):
            try:
                return f(*args, **kwargs)
            except:
                sleep(10 * attempt)

    return wrapped_f



counter = 0
@retry
def test ():
    counter += 1
    if counter < 4:
        raise ValueError('Error: '+counter)
    print('worked')

if __name__ == '__main__':
    test()
