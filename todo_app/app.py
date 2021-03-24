from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
from todo_app.data.session_items import *
from todo_app.flask_config import Config
from flask import request 
import requests
import os
import pdb
import json

app = Flask(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    query_params = {
        "key": os.environ.get('API_KEY'),
        "token": os.environ.get('TOKEN_KEY')
    }  
    url = f"https://api.trello.com/1/lists/{os.environ.get('TODO_LISTID')}/cards"
    todoitemsresponse = requests.get(url, params = query_params).json()
    todoitems = []
    for card in todoitemsresponse:
        myitem = Item(card['id'],card['idList'],card['name'])
        todoitems.append(myitem)
    return render_template('index.html', todoitems = todoitems)

@app.route('/add', methods=['POST'])
def add():
    query_params = {
        "key": os.environ.get('API_KEY'),
        "token": os.environ.get('TOKEN_KEY'),
        "idList": os.environ.get('TODO_LISTID'),
        "name": request.form.get('title')
    }
    url = "https://api.trello.com/1/cards"
    requests.post(url, params=query_params)
    return redirect(url_for("index"))
    
@app.route('/complete_item', methods=['POST'])
def complete_item():
          
    url = f"https://api.trello.com/1/cards/{request.form.get('id')}"
    query_params = {
        "key": os.environ.get('API_KEY'),
        "token": os.environ.get('TOKEN_KEY'),
        "idList": os.environ.get('DONE_LISTID')
    }  
    requests.put(url, params=query_params)
        
    return redirect(url_for("index"))


@app.route('/completeitem/<id>', methods=['GET','POST'])
def completeitem(id):
    url = f"https://api.trello.com/1/cards/{id}"
    query_params = {
        "key": os.environ.get('API_KEY'),
        "token": os.environ.get('TOKEN_KEY'),
        "idList": os.environ.get('DONE_LISTID')
    }

    requests.put(url, params=query_params)
    
    return redirect(url_for("index"))
  
if __name__ == '__main__':
    app.run()

class Item:
    def __init__(self, id, listid, title) :
        self.id = id
        self.listid = listid
        self.title = title
        if self.listid == os.environ.get('TODO_LISTID'):
            self.status = "ToDo" 
        elif self.listid == os.environ.get('DOING_LISTID'):
            self.status = "Doing" 
        elif self.listid == os.environ.get('DONE_LISTID'):
            self.status = "Done" 
        else: 
            self.status = "NotValid" 
        

