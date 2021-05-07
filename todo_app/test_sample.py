import pytest

@pytest.fixture
def createitems():
    _DEFAULT_ITEMS = [
        {'id':1,'status': 'Not Started', 'title': 'List saved todo items'},
        {'id':2,'status': 'Not Started', 'title': 'List saved doing items'},
        {'id':3,'status': 'Completed', 'title': 'List saved completed items'}
    ]




def test_doneitems():
    items = [
        {'id':1,'status': 'Not Started', 'title': 'List saved todo items'},
        {'id':2,'status': 'Not Started', 'title': 'List saved doing items'},
        {'id':3,'status': 'Completed', 'title': 'List saved completed items'}
    ]
    assert view_model.completed_items().count == 1