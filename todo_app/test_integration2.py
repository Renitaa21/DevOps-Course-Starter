from unittest import mock
from unittest.mock import patch

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')

def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/123/lists':
        response = mock()
        # sample_trello_lists_response should point to some test response data
        response.json.return_value = "sample_trello_lists_response"
        return response
    return None