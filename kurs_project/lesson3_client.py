import socket
import yaml
import hashlib
from argparse import ArgumentParser
import json
from datetime import datetime

READ_MODE = 'read'
WRITE_MODE = 'write'

def requsts(action, data, token=None):
    return {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp(),
        'token': token
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

parser.add_argument(
    '-ht', '--host', type=str, required=False,
    help='Sets sever host'
)

parser.add_argument(
    '-p', '--port', type=int, required=False,
    help='Sets server port  '
)

parser.add_argument(
    '-m', '--mode', type=str, required=False, default=READ_MODE,
    help='Sets cline mode  '
)

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

if args.host:
    config['host'] = args.host

if args.port:
    config['port'] = args.port

if __name__ == '__main__':
    try:

        s = socket.socket()  # создаём аналогичный сокет у клиента
        s.connect((config.get('host'), config.get('port')))  # коннектимся с сервисом
        while True:
            if args.mode == WRITE_MODE:
                action = input('введите action ')
                data = input('введите данные ')
        
                hash_obj = hashlib.sha256()
                hash_obj.update(
                    str(datetime.now().timestamp()).encode()
                )

                request = requsts(action, data, hash_obj.hexdigest())
                s.send(json.dumps(request).encode())
        
            else:          
                bite_resp = s.recv(config.get('buffer'))  # принимаем не более 2040 байт данных
                print(bite_resp.decode())
        
    except KeyboardInterrupt:
        print('server shutdown')
