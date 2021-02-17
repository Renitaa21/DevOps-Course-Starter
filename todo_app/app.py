from flask import Flask, render_template

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

todoitems = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

@app.route('/')
def index():
  
    return render_template('index.html', todoitems = todoitems)


if __name__ == '__main__':
    app.run()
