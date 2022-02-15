from stack import Stack


def rpn(*args):
    stack = Stack()
    for arg in args:
        if arg == "+":
            one = stack.pop()
            two = stack.pop()
            stack.push(one + two)
        elif arg == "*":
            one = stack.pop()
            two = stack.pop()
            stack.push(one * two)
        elif arg == "-":
            one = stack.pop()
            two = stack.pop()
            stack.push(two - one)
        else:
            stack.push(arg)
    return stack.pop()
