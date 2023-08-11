import datetime
import json

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.creation_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_json(), f)

    def to_json(self):
        return {'id': self.id, 'title': self.title, 'body': self.body}

    def delete(self):
        del self.to_json()

    @staticmethod
    def from_json(json_data):
        id = json_data['id']
        title = json_data['title']
        body = json_data['body']
        creation_date = datetime.datetime.strptime(json_data['creation_date'], '%Y-%m-%d %H:%M:%S')
        modification_date = datetime.datetime.strptime(json_data['modification_date'], '%Y-%m-%d %H:%M:%S')
        note = Note(id, title, body)
        note.creation_date = creation_date
        note.modification_date = modification_date
        return note
