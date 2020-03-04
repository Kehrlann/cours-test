class Set:
    def __init__(self):
        self._empty = True
        self._size = 0

    def empty(self):
        return self._empty

    def add(self, element):
        self._empty = False
        self._size += 1

    def size(self):
        return self._size
