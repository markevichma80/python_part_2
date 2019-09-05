from datetime import datetime

from decorator import logged

@logged('%(name)s - %(response)s')
def valid_request(request):
    if 'action' in request and 'time' in request:
        return True
    return False

@logged('%(name)s - %(response)s')
def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'code': code,   
        'data': data
    }