class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):
    def __init__(self, r=None):
        self.root_node = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root_node)
        self.root_node = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root_node
        prev_node = None

        while this_node is not None:  # while not at the end of the list
            if this_node.get_data() == d:
                if prev_node is not None:  # if we are the root node
                    prev_node.set_next(
                        this_node.get_next())  # as the root node is deleted, the next node of the new root node is at 2 nodes away to the right
                else:
                    self.root_node = this_node.get_next()  # the node at position 1 become the root node at position 0
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False

    def find(self, d):
        this_node = self.root_node
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() is None:
                return False
            else:
                this_node = this_node.get_next()


nodes = [Node(i) for i in range(50)]

test_list = LinkedList()

for node, next_node in zip(nodes, nodes[1:]):
    node.next_node = next_node
nodes[49].set_next(nodes[21])

def loop_size(test_node):
    temp = True
    new_node = test_node
    result = []
    while temp:
        result.append(new_node)
        new_node = new_node.get_next()
        if new_node in result:
            temp = False
            loop_size = len(result) - result.index(new_node.get_next()) + 1

    return loop_size

print(loop_size(nodes))
