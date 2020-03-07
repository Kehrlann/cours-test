class Set:
    def __init__(self):
        self._elements = []

    def empty(self):
        return len(self._elements) == 0

    def add(self, element):
        self._elements.append(element)

    def __len__(self):
        return len(self._elements)

    def contains(self, element):
        return element in self._elements

    def __iter__(self):
        for element in self._elements:
            yield element

