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

def insert_sort(head):
    if not head:
        return None
    if not head.next:
        return head.data

    list_temp = list()
    while head:
        list_temp.append(head)
        head = head.next
    sorted_list = sorted(list_temp, key=lambda node: node.data, reverse=True)
    head = None
    for node in sorted_list:
        node_temp = push(head, node)
        head = node_temp

    return head
