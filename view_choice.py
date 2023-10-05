import add_note
import delete_note
import edit_note
import working_file
import add_note
import show_note


def choice_user():
    flag = True
    while flag:
        choice = input('0 - создать файл\n'
                       '1 - создать заметку\n'
                       '2 - сохранить заметку\n'
                       '3 - прочитать все заметки\n'
                       '4 - редактировать заметку\n'
                       '5 - удалить заметку\n'
                       '6 - выход\n'
                       'Сделайте Ваш выбор: ')
        match choice:
            case '0':
                working_file.open_file()


            case '1':
                add_note.add()

            case '2':
                working_file.save_file()

            case '3':
                show_note.show_notepad()

            case '4':
                search = input('Что будем редактировать? Введите номер заметки. ')
                edit_note.edit(search)

            case '5':
                search = input('Что будем удалять? Введите номер заметки. ')
                delete_note.delete(search)

            case '6':
                flag = False
            case _:
                print('такой команды нет.')

