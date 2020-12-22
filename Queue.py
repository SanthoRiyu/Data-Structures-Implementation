from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


q = Queue()
q.enqueue({
    'company': 'TCS',
    'timestamp': '20 Dec, 09.01 AM',
    'price': 131.10
})
q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '20 Dec, 09.02 AM',
    'price': 132
})
q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '20 Dec, 09.03 AM',
    'price': 135
})

print(q.size())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())