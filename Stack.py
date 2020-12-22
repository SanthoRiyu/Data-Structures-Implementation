from collections import deque


# stack = deque()
#
# stack.append('A')
# stack.append('B')
# stack.append('C')
# stack.append('D')
# stack.append('E')
#
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(val):
    rev = ''
    stack = Stack()
    if len(val) > 0:
        for x in val:
            stack.push(x)
    for y in range(len(val)):
        rev += stack.pop()

    return rev


print(reverse_string("We will conquer COVID-19"))



