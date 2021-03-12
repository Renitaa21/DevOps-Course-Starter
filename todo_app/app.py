from flask import Flask, render_template
from werkzeug.utils import redirect
from todo_app.data.session_items import *
from todo_app.flask_config import Config
from flask import request 
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    todoitemsresponse = requests.get("https://api.trello.com/1/lists/6047ecb966a18d23e8029cd2/cards?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')).json()
    todoitems = []
    for obj in todoitemsresponse:
        cardname = obj['name']
        todoitems.append(cardname)
    return render_template('index.html', todoitems = todoitems)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        URL = "https://api.trello.com/1/cards?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd2&name=" + request.form.get('title')
        requests.post(URL)
        return redirect("http://127.0.0.1:5000/")
    else:
        pass
    
@app.route('/move', methods=['POST'])
def move():
    if request.method == 'POST':
        URL = "https://api.trello.com/1/cards/"+request.form.get('id')+"?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd4"
        requests.put(URL)
        return redirect("http://127.0.0.1:5000/")
    else:
        pass

if __name__ == '__main__':
    app.run()
