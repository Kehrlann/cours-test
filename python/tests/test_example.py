#####################
# "real" code"      #
#####################
def increment(value):
    return value + 1

#####################
# Here be our tests #
#####################
import pytest

def test_increment():
    assert increment(5) == 6
    assert increment(-5) == -4

def test_wrong_type():
    with pytest.raises(TypeError):
        increment()
