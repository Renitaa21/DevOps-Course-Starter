from flask import Flask, app, render_template, url_for
from werkzeug.utils import redirect
from todo_app.data.session_items import *
from todo_app.flask_config import Config
from flask import request 
import requests
import os
import pdb
import json
from todo_app.view_model import ViewModel
from todo_app.item import Item

def create_app():
    app = Flask(__name__)
    app.config.from_object('todo_app.flask_config.Config')
    
    @app.route('/')
    def index():
        query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY')
        }  
        url = f"https://api.trello.com/1/lists/{os.environ.get('TODO_LISTID')}/cards"
        itemsresponse = requests.get(url, params = query_params).json()
        items = []
        for card in itemsresponse:
            myitem = Item.from_trello_card(card)
            items.append(myitem)
        view_model = ViewModel(items)
        return render_template('index.html',view_model=view_model)

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

    _DEFAULT_ITEMS = [
            {'id':1,'status': 'Not Started', 'title': 'List saved todo items'},
            {'id':2,'status': 'Not Started', 'title': 'List saved doing items'},
            {'id':3,'status': 'Completed', 'title': 'List saved completed items'}
        ]
    return app


