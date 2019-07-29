
task_1 = ['разработка', 'сокет', 'декоратор']
for i in task_1:
    print(i,i.encode('utf-8'))
print('-'*50)
word_4, word_5, word_6 = [b'class', b'function', b'method']
print(word_4, word_5, word_6, '-'*50, sep='\n')
task_3 = ['attribute', 'класс', 'функция', 'type']
for x in task_3:
    print(x,x.encode('utf-8'))
print('-'*50)
task_4 = ['разработка', 'администрирование', 'protocol', 'standard']
for y in task_4:
    print(y, y.encode('utf-8').decode())
