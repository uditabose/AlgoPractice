#!/usr/local/bin/python3

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def __repr__(self):
        return str(self.items)

class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

        print(self.maxes_stack)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()


def largest_stack():
    """
    https://www.interviewcake.com/question/python/largest-stack

    Time :
    Space:
    Note :
    """
    max_stack = MaxStack()
    for item in [1, 2, 3, 4, 5]:
        max_stack.push(item)

    max_stack.pop()
    print(max_stack.get_max())
    max_stack.pop()
    print(max_stack.get_max())
    max_stack.pop()
    print(max_stack.get_max())
    max_stack.pop()
    print(max_stack.get_max())
    max_stack.pop()
    print(max_stack.get_max())

def run():
    largest_stack()


if __name__ == '__main__':
    run()
