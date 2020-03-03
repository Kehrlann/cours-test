#####################
# "real" code"      #
#####################
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


#####################
# Here be our tests #
#####################
def test_emptiness():
    empty = Set()
    one = Set()

    one.add("1")

    assert empty.empty() is True
    assert one.empty() is False

def test_size():
    empty = Set()
    one = Set()
    many = Set()

    one.add("1")
    many.add("1")
    many.add("2")

    assert empty.size() == 0
    assert one.size() == 1
    assert many.size() > 1

