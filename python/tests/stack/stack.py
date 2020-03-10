class ArrayStack:
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

    def __len__(self):
        return len(self._elements)


class Stack:
    class Link:
        def __init__(self, value, previous):
            self.value = value
            self.previous = previous

    def __init__(self):
        self._size = 0
        self._top = None

    def empty(self):
        return self._top == None

    def push(self, element):
        self._empty = False
        self._size += 1
        self._top = Stack.Link(element, self._top)

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

    def __len__(self):
        return self._size


class EmptyStackError(Exception):
    pass
