from datetime import datetime
from protocol import make_response

def date_control(request):
    return make_response(
        request, 200, datetime.now().timestamp()
        )
