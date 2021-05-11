class ViewModel():
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items

    def completed_items(self):
        completed_items = []
        for item in self.items:
            if item.status == "Completed":
                completed_items.append(item)
        return completed_items
    
    def todo_items(self):
        todo_items = []
        for item in self.items:
            if item.status == "To Do":
                todo_items.append(item)
        return todo_items

    def doing_items(self):
        doing_items = []
        for item in self.items:
            if item.status == "Doing":
                doing_items.append(item)
        return doing_items