import json
import logging

from resolvers import resolver
from protocol import valid_request, make_response




def handler_defold(bite_requ):
    request = json.loads(
        bite_requ.decode())

    if valid_request(request):
        action = request.get('action')
        control = resolver(action)
            
        if control:
            try:
                response = control(request)
                logging.debug(f'Client  send {request}')
            except Exception as arr:
                response = make_response(
                request, 500, 'Internal server arror '
                )
                logging.critical(f'{arr}')
        else:
            response = make_response(
            request, 404, f'Action {action} is not respons '
            )

            logging.error(f'client  call action with name {action}')
    else:
        response = make_response(
            request, 400, 'wrong request'
        )

        logging.error(f'client  send wrong request {request}')

    string_response = json.dumps(response)
    return string_response.encode()