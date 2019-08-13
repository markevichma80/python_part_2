import socket
import yaml
from argparse import ArgumentParser
import json
from datetime import datetime


def requsts(action, data):
    return {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp()
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
    '-p', '--port', type=str, required=False,
    help='Sets server port  '
)
args = parser.parse_args()
if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})
if __name__ == '__main__':
    try:
        s = socket.socket()  # создаём аналогичный сокет у клиента
        s.connect((config.get('host'), config.get('port')))  # коннектимся с сервисом
        action = input('введите action ')
        data = input('введите данные ')
        request = requsts(action, data)
        s.send(json.dumps(request).encode())
        bite_resp = s.recv(config.get('buffer'))  # принимаем не более 2040 байт данных
        print(bite_resp.decode())
        s.close()
    except KeyboardInterrupt:
        print('server shutdown')
