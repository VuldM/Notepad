import working_file


def show_notepad():
    note = working_file.open_file()
    for values in note.values():
        print(values)


