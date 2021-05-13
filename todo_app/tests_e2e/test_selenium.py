from todo_app.test_integrate import mock_get_lists
from todo_app import app
import pytest
import os
from threading import Thread
from todo_app.item import Item
import requests
from dotenv import load_dotenv,find_dotenv

@pytest.fixture(scope='module')
def app_with_temp_board():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

@pytest.fixture
def test_client():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

def create_trello_board():
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),
            "name": os.environ.get('TEST_BOARD_NAME')
        }  
    url = f"https://api.trello.com/1/boards/"
    boardresponse = requests.post(url, params = query_params).json()

def delete_trello_board(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
           "token": os.environ.get('TOKEN_KEY'),
       }  
    #url = f"https://api.trello.com/1/members/{username}/boards/"
    #boardidresponse = requests.post(url, params = query_params).json()
    #items = []
    #for board in boardidresponse:
     #   if (board.name == os.environ.get('TEST_BOARD_NAME')):
      #      boardid = board.id
    
    url = f"https://api.trello.com/1/boards/{board_id}/"
    boarddelresponse = requests.delete(url, params = query_params).json()