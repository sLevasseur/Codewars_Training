class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

#the fastest one
def remove_duplicates(head):
    temp_node = head
    if not head:
        return None
    while temp_node.next is not None:
        if temp_node.data == temp_node.next.data:
            temp_node.next = temp_node.next.next
        else:
            temp_node = temp_node.next
    return head

def push(head, data):
    if head:
        new_node = Node(data)
        new_node.next = head
        head = new_node
        return head

    return Node(data)

#slow one : O(2n)
def remove_duplicates(head):
    duplicate_list = list()
    while head:
        if head.data not in duplicate_list:
            duplicate_list.insert(0, head.data)
        head = head.next
    for node in duplicate_list:
        node_temp = push(head, node)
        head = node_temp
    return head

#recurisve
def remove_duplicates_recursion(head):
    if not head or not head.next:
        return head
    if head.next != None:
        if head.data == head.next.data:
            to_free = head.next
            head.next=head.next.next
            remove_duplicates(head)
        else:
            remove_duplicates(head.next)
    print(head.data)
    return head
