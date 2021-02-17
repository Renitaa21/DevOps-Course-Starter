from flask import Flask, render_template
from todo_app.data.session_items import *
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    todoitems = get_items()
    return render_template('index.html', todoitems = todoitems)


if __name__ == '__main__':
    app.run()
