from stack import Stack, EmptyStackError
import pytest


def test_create():
    assert Stack() is not None


def test_empty():
    empty = Stack()
    not_empty = Stack()

    not_empty.push("something")

    assert empty.empty() is True
    assert not_empty.empty() is False


def test_size():
    empty = Stack()
    two = Stack()

    two.push("one")
    two.push("deux")

    assert len(empty) == 0
    assert len(two) == 2


def test_peek():
    stack = Stack()

    stack.push("one")
    stack.push("deux")

    assert stack.peek() == "deux"
    with pytest.raises(EmptyStackError):
        Stack().peek()


def test_pop():
    stack = Stack()

    stack.push("one")
    stack.push("two")
    stack.push("three")

    assert stack.peek() == "three"
    assert stack.pop() == "three"
    assert stack.peek() == "two"
    assert len(stack) == 2

    with pytest.raises(EmptyStackError):
        Stack().pop()


def test_clone():
    stack = Stack()
    stack.push("one")
    stack.push("two")

    cloned_stack = stack.clone()

    cloned_contents = [cloned_stack.pop(), cloned_stack.pop()]
    assert cloned_contents == ["two", "one"]
    assert len(cloned_stack) == 0
    assert len(stack) == 2
