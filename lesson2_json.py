import json
import datetime

with open('orders.json', 'r+') as file:
    data = json.load(file)
    item_ = 0
    while True:
        item_ = input('Введите наименование товара, или нет для завершения введения: ').capitalize()
        if item_ == 'Нет':
            break
        quantity_ = int(input('Введите количество: '))
        price_ = float(input('Введите цену: '))
        buyer_ = input('Введите покупателя: ')
        date_ = datetime.datetime.now()
        data['orders'].append(
            {'item': f'{item_}', 'quantity': f'{quantity_}', 'price': f'{price_}', 'buyer': f'{buyer_}',
             'date': f'{date_}'})
    json.dump(data, file, indent=4)
