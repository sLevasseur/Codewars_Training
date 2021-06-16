class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count

def count(node, data):
    count = 0
    while node:
        if node.data == data:
            count += 1
        node = node.next

    return count
