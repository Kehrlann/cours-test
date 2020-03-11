class ListStack:
    def __init__(self):
        self._elements = []

    def empty(self):
        return len(self._elements) == 0

    def push(self, element):
        self._elements.append(element)

    def peek(self):
        if self.empty():
            raise EmptyStackError()
        return self._elements[-1]

    def pop(self):
        if self.empty():
            raise EmptyStackError()
        return self._elements.pop()

    def clone(self):
        clone = ListStack()
        clone._elements = [x for x in self._elements]
        return clone

    def __len__(self):
        return len(self._elements)


class LinkedStack:
    class Link:
        def __init__(self, value, previous):
            self.value = value
            self.previous = previous

        def clone(self):
            cloned_previous = None if self.previous is None else self.previous.clone()
            clone = LinkedStack.Link(self.value, cloned_previous)
            return clone

    def __init__(self):
        self._size = 0
        self._top = None

    def empty(self):
        return self._top is None

    def push(self, element):
        self._size += 1
        self._top = LinkedStack.Link(element, self._top)

    def peek(self):
        if self.empty():
            raise EmptyStackError()
        return self._top.value

    def pop(self):
        if self.empty():
            raise EmptyStackError()
        value = self._top.value
        self._top = self._top.previous
        self._size -= 1
        return value

    def clone(self):
        clone = LinkedStack()
        clone._top = self._top.clone()
        clone._size = self._size
        return clone

    def __len__(self):
        return self._size


class EmptyStackError(Exception):
    pass


class Stack(ListStack):
    pass
