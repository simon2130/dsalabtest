class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
linked_list = LinkedList()
for i in range(1, 6):
    linked_list.append(i)

print("Original list:")
current = linked_list.head
while current:
    print(current.data)
    current = current.next

linked_list.reverse()

print("\nReversed list:")
current = linked_list.head
while current:
    print(current.data)
    current = current.next
