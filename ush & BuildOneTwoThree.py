class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    if head:
        new_node = Node(data, head)
        new_node.next = head
        head = new_node
        return head

    return Node(data)


def build_one_two_three():
    list_to_build = [3, 2, 1]
    head = None

    for node in list_to_build:
        node_temp = push(head, node)
        head = node_temp

    return head
