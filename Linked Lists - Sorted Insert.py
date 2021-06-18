class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if not head or head.data > data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    head.next = sorted_insert(head.next, data)

    return head


""" head_node = head
    while head:
        try:
            if head.data < data < head.next.data:
                new_pointer = head.next
                new_node = Node(data)
                new_node.next = new_pointer
                head.next = new_node
                head = head.next
            else:
                head = head.next
        except AttributeError:
            new_pointer = None
            new_node = Node(data)
            new_node.next = new_pointer
            head.next = new_node
            head = head.next

    return head_node
"""
