class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    if not node:
        return "None linked list should throw error."
    while index != 0:
        node = node.next
        index -= 1

    return node if not node else "Invalid index value should throw error."
