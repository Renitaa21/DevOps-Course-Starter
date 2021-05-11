import pytest
from todo_app.view_model import ViewModel
from todo_app.item import Item

# @pytest.fixture
# def createitems():
#     _DEFAULT_ITEMS = [
#         {'id':1,'status': 'Not Started', 'title': 'List saved todo items'},
#         {'id':2,'status': 'Not Started', 'title': 'List saved doing items'},
#         {'id':3,'status': 'Completed', 'title': 'List saved completed items'}
#     ]




def test_doneitems():
    items = [
        Item(1, 'List saved todo items', 'Todo'),
        Item(2, 'List saved doing items', 'Doing'),
        Item(3, 'List saved completed items', 'Completed')
    ]

    view_model = ViewModel(items)

    assert view_model.completed_items().count == 1