from datetime import datetime
def valid_request(request):
    if 'action' in request and 'time' in request:
        return True
    return False


def make_response(request, code, data=None):
    return {
        'data': request.get('data'),
        'time': datetime.now().timestamp(),
        'code': code,
        'data': data
    }