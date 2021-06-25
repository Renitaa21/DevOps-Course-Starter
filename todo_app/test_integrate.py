from todo_app import app
from unittest.mock import patch,Mock
import pytest
from dotenv import load_dotenv,find_dotenv
import os
#import requests

@pytest.fixture
def test_client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, test_client):
    # Replace call to requests.get(url) with our own function
    #Arrange
    query_params = {
                "key": os.environ.get('API_KEY'),
                "token": os.environ.get('TOKEN_KEY')
            }  
    url = "https://api.trello.com/1/boards/123/lists"
    #Act
    mock_get_requests.side_effect = mock_get_lists(url, params=query_params)
    response = test_client.get('/')
    #assert needs to go here 
    assert response.status_code == 200

#not a test just a function
def mock_get_lists(url, params):
    if url == f"https://api.trello.com/1/boards/{os.environ.get('TESTBOARDID')}/lists":
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        sample_trello_lists_response = [
    {
        "id": "6047ecb966a18d23e8029cd2",
        "name": "To Do",
        "closed": False,
        "pos": 16384,
        "softLimit": None,
        "idBoard": "6047ecb966a18d23e8029cd1",
        "subscribed": False
    },
    {
        "id": "6047ecb966a18d23e8029cd3",
        "name": "Doing",
        "closed": False,
        "pos": 32768,
        "softLimit": None,
        "idBoard": "6047ecb966a18d23e8029cd1",
        "subscribed": False
    },
    {
        "id": "6047ecb966a18d23e8029cd4",
        "name": "Done",
        "closed": False,
        "pos": 49152,
        "softLimit": None,
        "idBoard": "6047ecb966a18d23e8029cd1",
        "subscribed": False
    }
]

        response.json.return_value = sample_trello_lists_response
        return response
    return None

#Set null to None, true to True, false to False, get valid response and add that in sample_trello_lists_response 