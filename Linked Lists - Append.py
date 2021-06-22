# https://www.codewars.com/kata/linked-lists-append
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if not listA and not listB:
        return None
    head = listA
    while listA:
        listA = listA.next
    listA.next = listB

    return head
