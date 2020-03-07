#####################
# "real" code"      #
#####################
def increment(value):
    return value + 1

#####################
# Here be our tests #
#####################
def test_increment():
    assert increment(5) == 6
    assert increment(-5) == -4
