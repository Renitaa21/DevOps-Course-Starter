from todo_app.test_integrate import mock_get_lists
from todo_app import app
import pytest
import os
from threading import Thread
from todo_app.item import Item
import requests
from dotenv import load_dotenv,find_dotenv
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope='module')
def app_with_temp_board():
    # Create the new board & update the board id environment variable
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id
    # list_id = create_trello_list(board_id)
    # create_trello_card(list_id)
    todolist_id = getToDoListid(board_id)
    os.environ['TODO_LISTID'] = todolist_id
    donelist_id = getDoneListid(board_id)
    os.environ['DONE_LISTID'] = donelist_id
    doinglist_id = getDoingListid(board_id)
    os.environ['DOING_LISTID'] = doinglist_id
    # create_trello_card(todolist_id)
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

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey_completeitem(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    title_input_elem = driver.find_element_by_name("title")
    title_input_elem.send_keys("Test Todo")
    title_input_elem.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    elem = driver.find_element_by_name("complete-button")
    elem.click()

    time.sleep(5)
    assert (driver.title == 'To-Do App' and "Test Todo" not in driver.page_source)

def test_task_journey_createitem(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    title_input_elem = driver.find_element_by_name("title")
    title_input_elem.send_keys("Test Todo")
    title_input_elem.send_keys(Keys.RETURN)

    time.sleep(5)

    assert (driver.title == 'To-Do App'and "Test Todo" in driver.page_source)

def create_trello_board():
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),
            "name": os.environ.get('TEST_BOARD_NAME')
        }  
    url = f"https://api.trello.com/1/boards/"
    boardresponse = requests.post(url, params = query_params).json()
    return boardresponse['id']

def create_trello_list(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),
            "name": os.environ.get('TEST_LIST_NAME'),
            "idBoard": board_id
        } 
    listurl = f"https://api.trello.com/1/lists/"
    listresponse = requests.post(listurl, params = query_params).json()
    return listresponse['id']

def create_trello_card(listid):
    query_params_card = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),
            "idList": listid,
            "name": os.environ.get('TEST_CARD_NAME')  
        }
    url = f"https://api.trello.com/1/cards/"
    cardresponse = requests.post(url, params = query_params_card).json()

def getToDoListid(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),    
            "idBoard": board_id
        } 
    url = f"https://api.trello.com/1/boards/{board_id}/lists/"
    listsresponse = requests.get(url, params = query_params).json()
    for list in listsresponse:
        if list['name'] == 'To Do':
            return list['id']
    return None

def getDoneListid(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),    
            "idBoard": board_id
        } 
    url = f"https://api.trello.com/1/boards/{board_id}/lists/"
    listsresponse = requests.get(url, params = query_params).json()
    for list in listsresponse:
        if list['name'] == 'Done':
            return list['id']
    return None

def getDoingListid(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
            "token": os.environ.get('TOKEN_KEY'),    
            "idBoard": board_id
        } 
    url = f"https://api.trello.com/1/boards/{board_id}/lists/"
    listsresponse = requests.get(url, params = query_params).json()
    for list in listsresponse:
        if list['name'] == 'Doing':
            return list['id']
    return None


def delete_trello_board(board_id):
    query_params = {
            "key": os.environ.get('API_KEY'),
           "token": os.environ.get('TOKEN_KEY'),
       }  
    #incase boardid was not provided
    #url = f"https://api.trello.com/1/members/{username}/boards/"
    #boardidresponse = requests.post(url, params = query_params).json()
    #items = []
    #for board in boardidresponse:
     #   if (board.name == os.environ.get('TEST_BOARD_NAME')):
      #      boardid = board.id
    
    url = f"https://api.trello.com/1/boards/{board_id}/"
    boarddelresponse = requests.delete(url, params = query_params).json()