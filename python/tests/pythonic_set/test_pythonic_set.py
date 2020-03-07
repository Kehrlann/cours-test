from pythonic_set import Set
import pytest


@pytest.fixture
def empty():
    return Set()


@pytest.fixture
def one():
    one = Set()
    one.add("1")
    return one


@pytest.fixture
def many():
    many = Set()
    many.add("1")
    many.add("2")
    return many


def test_emptiness(empty, one):
    assert empty.empty() is True
    assert one.empty() is False


def test_size(empty, one, many):
    assert len(empty) == 0
    assert len(one) == 1
    assert len(many) > 1

def test_contains(empty, one, many):
    assert not empty.contains("1")
    assert not empty.contains("2")
    assert one.contains("1")
    assert not one.contains("2")
    assert many.contains("1")
    assert many.contains("2")

