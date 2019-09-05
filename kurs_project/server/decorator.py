from functools import wraps
import logging



logger = logging.getLogger('server.decorator')

def logged(log_form):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            response = func(*args)
            logger.debug(log_form % {'name': func.__name__, 'args': args,  'response': response})
            return response
        return wrapper
    return decorator



