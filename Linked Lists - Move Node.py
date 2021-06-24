class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    temp_node = source
    source = source.next
    temp_node.next = dest
    dest = temp_node
    return Context(source, dest)

def move_node_better(source, dest):
    if source is None: raise ValueError
    return Context(source.next, Node(source.data, dest))
