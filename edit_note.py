import add_note
import working_file


def edit(searched: int):
    note = working_file.open_file()
    searched = str(searched)
    for item in note.keys():
        if item == searched:
            print(f"id - {note.get(searched)['id']}\nдата - {note.get(searched)['date']}\nзаголовок - {note.get(searched)['title']}\nтекст = {note.get(searched)['text']}\n")
            id = int(searched)
            date = note[searched]['date']
            title = input('Измените заголовок  ')
            text = input('Измените текст  ')
            add_note.notepad[searched] = {'id': id, 'date': str(date), 'title': title, 'text': text}
