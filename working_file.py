import json

import add_note

path = 'C:/Users/aniai/PycharmProjects/pythonProject/Notepad.json'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    print('Файл открыт')
    return data


def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(add_note.notepad, file, indent=4, ensure_ascii=False)


