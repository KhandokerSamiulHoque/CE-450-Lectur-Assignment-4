class LinkedList:
    def __init__(self, node, next_node=None):
        self.node = node
        self.next_node = next_node


def prnt_lnk(s):
    new_list = []
    current = s
    
    while current:
        new_list.append(current.node)
        current = current.next_node
    return "<" + " ".join(map(str, new_list)) + ">"

def link(node, next_node=None):
    return LinkedList(node, next_node)


def empty():
    return None
output = prnt_lnk(link(1, link(2, link(3, link(4, empty())))))
print(output)