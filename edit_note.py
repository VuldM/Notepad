import add_note
import working_file


def edit(searched: int):
    for item in add_note.notepad.keys():
        if item == searched:
            print(add_note.notepad.get(searched))
            id = int(searched)
            date = add_note.notepad[searched]['date']
            title = input('Измените заголовок  ')
            text = input('Измените текст  ')
            add_note.notepad[searched] = {'id': id, 'date': str(date), 'title': title, 'text': text}
