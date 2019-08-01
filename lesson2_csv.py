import re
import os
import csv


def doc_text(text_, list_):
    search_t = re.search('Изготовите|Название|Код|Тип', text_)
    if search_t:
        list_.append([text_.split(':')[0], text_.split(':')[1].strip(' ')])
        return list_


list_1 = ['os_prod_list', 'os_name_list', 'os_code_list', 'os_type_list']
data_ = input('Название папки:')


def get_data(data_):
    list_ = []
    for i in range(len(os.listdir(f'{data_}'))):
        with open(os.listdir(f'{data_}')[i], 'r') as t:
            for text_ in t:
                doc_text(text_, list_)
    os_prod_list = [list_[i][1] for i in range(len(list_)) if list_[i][0] == 'Название ОС']
    os_name_list = [list_[i][1] for i in range(len(list_)) if list_[i][0] == 'Изготовитель ОС']
    os_code_list = [list_[i][1] for i in range(len(list_)) if list_[i][0] == 'Код продукта']
    os_type_list = [list_[i][1] for i in range(len(list_)) if list_[i][0] == 'Изготовитель системы']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(len(os_prod_list)):
        main_data.append(
            [os_prod_list[i].replace('\n', ''), os_name_list[i].replace('\n', ''), os_code_list[i].replace('\n', ''),
             os_type_list[i].replace('\n', '')])
    return main_data


print(get_data(data_))


def write_to_csv(data_):
    with open('write.csv', 'w') as file:
        writer = csv.writer(file)
        for row in get_data(data_):
            writer.writerow(row)


write_to_csv('data')
