import model

def start():
    input_from_user = ''
    while input_from_user != '7':
        model.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            model.show('all')
        if input_from_user == '2':
            model.add()
        if input_from_user == '3':
            model.show('all')
            model.id_edit_del_show('del')
        if input_from_user == '4':
            model.show('all')
            model.id_edit_del_show('edit')
        if input_from_user == '5':
            model.show('date')
        if input_from_user == '6':
            model.show('id')
            model.id_edit_del_show('show')
        if input_from_user == '7':
            print("До свидания!")
            break