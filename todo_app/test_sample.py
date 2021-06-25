import pytest
from todo_app.view_model import ViewModel
from todo_app.item import Item

def test_doneitems():
    items = [
        Item(1, 'List saved todo items', 'To Do'),
        Item(2, 'List saved doing items', 'Doing'),
        Item(3, 'List saved completed items', 'Completed')
    ]

    view_model = ViewModel(items)
    
    assert len(view_model.completed_items()) == 1


def test_todoitems():
    items = [
        Item(1, 'List saved todo items', 'To Do'),
        Item(2, 'List saved doing items', 'Doing'),
        Item(3, 'List saved completed items', 'Completed'),
        Item(4, 'List saved doing items 2', 'Doing')
    ]

    view_model = ViewModel(items)
    
    assert len(view_model.todo_items()) == 1


def test_doingitems():
    items = [
        Item(1, 'List saved todo items', 'To Do'),
        Item(2, 'List saved doing items', 'Doing'),
        Item(3, 'List saved completed items', 'Completed'),
        Item(4, 'List saved doing items 2', 'Doing')
    ]

    view_model = ViewModel(items)
    
    assert len(view_model.doing_items()) == 2