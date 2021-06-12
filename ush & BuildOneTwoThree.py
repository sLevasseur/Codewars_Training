class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):  # create a Node
    new_head = Node(data)
    if not head:
        return new_head
    new_head.next = head
    return new_head

def build_one_two_three():  # create a list
    data_list = [3, 2, 1]
    head = None
    for data in data_list:
        head = push(head, data)

    return head

