import os

class Item:
    def __init__(self, id, title, status) :
        self.id = id
        self.title = title
        self.status = status

    @classmethod
    def from_trello_card(cls, card) :
        id = card['id']
        title = card['name']
        list_id = card['idList']
        status = ""

        if list_id == os.environ.get('TODO_LISTID'):
            status = "ToDo" 
        elif list_id == os.environ.get('DOING_LISTID'):
            status = "Doing" 
        elif list_id == os.environ.get('DONE_LISTID'):
            status = "Done" 
        else: 
            status = "NotValid" 

        return cls(id, title, status)