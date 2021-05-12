from todo_app.app import App
from unittest import mock
from unittest.mock import patch
import pytest
from dotenv import load_dotenv,find_dotenv
import requests
import os


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    app = App()
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    query_params = {
                "key": os.environ.get('API_KEY'),
                "token": os.environ.get('TOKEN_KEY')
            }  
    url = "https://api.trello.com/1/boards/123/lists"
    mock_get_requests.side_effect = mock_get_lists(url, params=query_params)
    response = client.get('/')

def mock_get_lists(url, params):
    if url == f"https://api.trello.com/1/boards/123/lists":
        response = mock()
        # sample_trello_lists_response should point to some test response data
        sample_trello_lists_response = " blahblahModifytobehavelikejson"
        response.json.return_value = sample_trello_lists_response
        return response
    return None