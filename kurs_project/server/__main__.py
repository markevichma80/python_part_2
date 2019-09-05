import socket
import yaml
from argparse import ArgumentParser
import json
import logging
import select

from handlers import handler_defold
from datetime import datetime
from protocol import valid_request, make_response
from resolvers import resolver



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
print(args)

if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        config.update(file_config or {})

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = (
        logging.FileHandler('sevrer.log'),
        logging.StreamHandler()
    )
)

request = []
connections = []

host, port = config.get('host'), config.get('port')

try:
    s = socket.socket()  # создаём сокет протокола TCP
    s.bind((host, port))  # присваиваем номар порта
    s.setblocking(False)
    s.settimeout(1)
    s.listen(10)  # максимальное количество подключений
    
    logging.info(f'{host}: {port}')

    while True:
        try:
            client, addr = s.accept()  # акцептим запрос на соединение
            client_host, client_port = addr
            logging.info(f'{client_host}: {client_port}')
            connections.append(client)
        except:
            print('fig')



        rlist, wlist, xlist = select.select(client, client, client, 0)

        for read_client in rlist:
            bite_requ = client.recv(config.get('buffer'))
            request.append(bite_requ)
        
        if request:
            bite_requ = request.pop()
            string_response = handler_defold(bite_requ)
        
            for write_client in wlist:
                write_client.send(string_response)
 
        #bite_requ = client.recv(config.get('buffer'))  # максимальное количество данных
        #string_response = handler_defold(bite_requ)
        #client.send(string_response)
        
except KeyboardInterrupt:
    logging.info('server shutdown')
