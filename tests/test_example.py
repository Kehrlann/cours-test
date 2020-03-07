#####################
# "real" code"      #
#####################
class Set:
    def __init__(self):
        self._empty = True

    def empty(self):
        return self._empty

    def add(self, element):
        self._empty = False

#####################
# Here be our tests #
#####################
def test_emptiness():
    empty = Set()
    one = Set()

    one.add("1")

    assert empty.empty() is True
    assert one.empty() is False

def test_fail():
    compare = 1 > 2
    assert compare is True
