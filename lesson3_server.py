import socket
import yaml
from argparse import ArgumentParser
import json
from datetime import datetime


def valid_rquest(request):
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


config = {
    'host': '127.0.0.1',
    'port': 7777,
    'buffer': 1024
}
parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)
args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

host, port = config.get('host'), config.get('port')
if __name__ == '__main__':
    try:
        s = socket.socket()  # создаём сокет протокола TCP
        s.bind((host, port))  # присваиваем номар порта
        s.listen(10)  # максимальное количество подключений
        while True:
            client, addr = s.accept()  # акцептим запрос на соединение
            client_host, client_port = addr
            print(client_host, client_port)
            bite_requ = client.recv(config.get('buffer'))  # максимальное количество данных
            request = json.loads(
                bite_requ.decode()
            )
            if valid_rquest(request):
                response = make_response(
                    request, 200, request.get('data')
                )
            else:
                response = make_response(
                    request, 400, 'wrong request'
                )
            string_response = json.dumps(response)

            client.send(string_response.encode())
            client.close()
    except KeyboardInterrupt:
        print('server shutdown')
