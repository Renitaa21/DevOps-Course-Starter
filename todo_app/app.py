from flask import Flask, render_template
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
    todoitemsresponse = requests.get("https://api.trello.com/1/lists/6047ecb966a18d23e8029cd2/cards?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')).json()
    todoitems = []
    for obj in todoitemsresponse:
        cardname = obj['name']
        todoitems.append(cardname)
    return render_template('index.html', todoitems = todoitems)

@app.route('/add', methods=['POST'])
def add():
    
    URL = "https://api.trello.com/1/cards?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd2&name=" + request.form.get('title')
    requests.post(URL)
    return redirect(url_for("index"))
    
@app.route('/complete_item', methods=['POST'])
def complete_item():
   
    #newURL = "https://api.trello.com/1/cards/"+id+"?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd4"
        
    URL = "https://api.trello.com/1/cards/"+request.form.get('id')+"?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd4"
      
    requests.put(URL)
        
    return redirect(url_for("index"))


@app.route('/completeitem/<name>', methods=['GET','POST'])
def completeitem(name):
    itemidURL = "https://api.trello.com/1/search?modelTypes=cards&query="+str(name)+"?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')
    
    itemidresp = requests.put(itemidURL)
    itemidjson = itemidresp.json()
    id = itemidjson['cards'][0]['id']

    URL = "https://api.trello.com/1/cards/"+str(id)+"?&key="+os.environ.get('API_KEY')+"&token="+os.environ.get('TOKEN_KEY')+"&idList=6047ecb966a18d23e8029cd4"
    requests.put(URL)
    
    return redirect(url_for("index"))
  
if __name__ == '__main__':
    app.run()
