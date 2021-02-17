from flask import Flask, render_template
from werkzeug.utils import redirect
from todo_app.data.session_items import *
from todo_app.flask_config import Config
from flask import request 

app = Flask(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    todoitems = get_items()
    return render_template('index.html', todoitems = todoitems)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        add_item(title=request.form.get('title'))
        return redirect("http://127.0.0.1:5000/")
    else:
        pass
    

if __name__ == '__main__':
    app.run()
