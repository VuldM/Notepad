import json

import add_note

path = 'C:/Users/aniai/PycharmProjects/pythonProject/Notepad.json'


def open_file():
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        print('Файл открыт')
        return data
    except IOError:
        print('Файл не существует!')
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(add_note.notepad, file, indent=4, ensure_ascii=False)

def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(add_note.notepad, file, indent=4, ensure_ascii=False)
