class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Link list is empty')
            return
        itr = self.head
        lir = ''

        while itr:
            lir += str(itr.data) + '-->'
            itr = itr.next
        print(lir)

    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for val in data_list:
            self.insert_at_last(val)
        return

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, val):
        if self.head is None:
            raise Exception('Linked list empty!!!')
        itr = self.head
        while itr:
            if val == itr.data:
                itr_prev.next = itr_prev.next.next
                break
            itr_prev = itr
            itr = itr.next

    def insert_after_value(self, val, ins_val):
        if self.head is None:
            raise Exception('Linked list empty!!!')

        itr = self.head
        while itr:
            if val == itr.data:
                itr.next = Node(ins_val, itr.next)
                break
            itr = itr.next


Llist = LinkedList()
Llist.insert_at_beginning('A')
Llist.insert_at_beginning('B')
Llist.insert_at_last('C')
Llist.insert_at_last('D')
Llist.insert_at_last('E')
Llist.insert_values(['w', 'x', 'y', 'z'])
Llist.print()
Llist.remove_at(2)
Llist.print()
Llist.insert_at(3, 'S')
Llist.print()
Llist.remove_by_value('D')
Llist.print()
Llist.remove_by_value('y')
Llist.print()
Llist.insert_after_value('S', 'y')
Llist.print()
