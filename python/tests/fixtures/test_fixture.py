import pytest


@pytest.fixture
def messages():
    messages = []
    messages.append("before test ...")
    yield messages
    messages.append("after test !")
    print(messages)


def test_stuff(messages):
    messages.append("Testing !")
