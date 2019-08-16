from protocol import make_response
def echo_controlers(request):
    data =request.get('data')
    return make_response(
                request, 200, data)