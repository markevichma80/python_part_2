from datetime import datetime

from protocol import make_response
from decorator import logged
from massenger.decor import login_chek

@login_chek
@logged('%(name)s-%(response)s')
def date_control(request):
    return make_response(
        request, 200, datetime.now().timestamp()
        )
