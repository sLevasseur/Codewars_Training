class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert_nth(head, index, data):
    if not head:
        head = Node(data)
        return head

    if index == 0:
        new_node = Node(data, head)
        head = new_node
        return head

    head_node = head
    while index != 1:
        head = head.next
        index -= 1

    new_pointer = head.next
    new_node = Node(data, new_pointer)
    head.next = new_node

    return head_node
