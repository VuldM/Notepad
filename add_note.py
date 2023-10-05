import datetime

notepad = {}


def next_id():
    for i in notepad.keys():
        i = int(i)
    i += 1
    return i


def add():
    id = next_id()
    date = datetime.datetime.now()
    title = input('Введите заголовок  ')
    text = input('Введите текст  ')
    notepad.setdefault(id, {'id': id, 'date': str(date), 'title': title, 'text': text})
    print(notepad)
