from protocol import make_response
from decorator import logged
from massenger.decor import login_chek

@login_chek
@logged('%(name)s - %(response)s')
def echo_controlers(request):
    data = request.get('data')
    return make_response(
                request, 200, data) 