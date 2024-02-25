import functools
import logging


def log_exception(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            err = "Exception in  "
            err += function.__name__
            logging.exception(err)
            # re-raise the exception
            raise
    return wrapper
