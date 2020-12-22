class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def print_forward(self):
        if self.head is None:
            print('Link list is empty')
            return
        itr = self.head
        lir = ''

        while itr:
            lir += str(itr.data) + '-->'
            itr = itr.next
        print(lir)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print('Link list is empty')
            return

        itr = self.get_last_node()
        lir = ''

        while itr:
            lir += str(itr.data) + '-->'
            itr = itr.prev
        print(lir)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data, None, itr)
        itr.next = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next, itr)
                itr.next.next.prev = itr.next
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
            itr = itr.next
            count += 1


Dub = DoublyLinkList()
Dub.insert_at_beginning('A')
Dub.insert_at_beginning('B')
Dub.insert_at_beginning('C')
Dub.insert_at_beginning('D')
Dub.insert_at_end('E')
Dub.print_forward()
Dub.print_backward()
Dub.insert_at(4, 'X')
Dub.print_forward()
Dub.print_backward()
Dub.remove_at(2)
Dub.print_forward()
Dub.print_backward()
