import notebook

number = 3

def menu():
    print("\nЭто программа 'Заметки'. Выберите необходимый пункт меню:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")

def add():
    note = create_note(number)
    array = read_file()
    for notes in array:
        if notebook.Note.get_id(note) == notebook.Note.get_id(notes):
            notebook.Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Заметка добавлена...')

def show(text):
    logic = True
    array = read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notebook.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notebook.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notebook.Note.get_date(notes):
                print(notebook.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')

def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = read_file()
    logic = True
    for notes in array:
        if id == notebook.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note(number)
                notebook.Note.set_title(notes, note.get_title())
                notebook.Note.set_body(notes, note.get_body())
                notebook.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(notebook.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    write_file(array, 'a')

def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(notebook.Note.to_string(notes))
        file.write('\n')
    file.close

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = notebook.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array

def create_note(number):
    title = check_len_text_input(
        input('Введите заголовок заметки: '), number)
    body = check_len_text_input(
        input('Введите текст заметки: '), number)
    return notebook.Note(title=title, body=body)

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text
