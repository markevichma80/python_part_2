from protocol import make_response
from functools import wraps


def login_chek(func):
    @wraps(func)
    def wrapper(request):        
        if 'token' in request and request.get('token'):
            return func(request)
        return make_response(request, 401, 'Not authenticated')
    return wrapper