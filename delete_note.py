import add_note
import working_file


def delete():
    add_note.notepad = working_file.open_file()
    note = working_file.open_file()
    if note:
        searched = input('Что будем удалять? Введите номер заметки. ')
        searched = str(searched)
        add_note.notepad.pop(searched)
        working_file.save_file()
    else:
        print('Тут нечего удалять')
