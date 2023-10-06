import datetime

import show_note
import working_file

notepad = {}


def next_id():
    if not notepad:
        i = 0
    else:
        for i in notepad.keys():
            i = int(i)
        i += 1
    return i


def add():
    uid = next_id()
    date = datetime.datetime.now()
    title = input('Введите заголовок  ')
    text = input('Введите текст  ')
    notepad.setdefault(uid, {'id': uid, 'date': str(date), 'title': title, 'text': text})
    working_file.save_file()
    show_note.show_notepad()
