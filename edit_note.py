import add_note
import working_file


def edit():
    add_note.notepad = working_file.open_file()
    note = working_file.open_file()
    if note:
        searched = input('Что будем редактировать? Введите номер заметки. ')
        searched = str(searched)
        for item in note.keys():
            if item == searched:
                print(f"id - {note.get(searched)['id']}\nдата - {note.get(searched)['date']}\nзаголовок - {note.get(searched)['title']}\nтекст = {note.get(searched)['text']}\n")
                id = int(searched)
                date = note[searched]['date']
                title = input('Измените заголовок  ')
                text = input('Измените текст  ')
                add_note.notepad[searched] = {'id': id, 'date': str(date), 'title': title, 'text': text}
                working_file.save_file()
    else:
        print('Тут нечего редактировать\n')
