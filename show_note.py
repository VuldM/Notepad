import add_note
import working_file


def show_notepad():
    note = working_file.open_file()
    add_note.notepad = note
    for item in add_note.notepad.values():
        print(item)

