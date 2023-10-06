import add_note
import delete_note
import edit_note
import working_file
import add_note
import show_note


def choice_user():
    add_note.notepad = working_file.open_file()
    flag = True
    while flag:
        choice = input('1 - создать заметку\n'
                       '2 - прочитать все заметки\n'
                       '3 - редактировать заметку\n'
                       '4 - удалить заметку\n'
                       '5 - выход\n'
                       'Сделайте Ваш выбор: ')
        match choice:
            case '1':
                add_note.add()
            case '2':
                show_note.show_notepad()
            case '3':
                edit_note.edit()
            case '4':
                delete_note.delete()
            case '5':
                flag = False
            case _:
                print('такой команды нет.')
