class LinkedList:
    def __init__(self, node, next=None):
        self.node = node
        self.next = next


def cntn_link(s, elm):
    current = s
    while current is not None:
        if current.node == elm:
            return True
        current = current.next
    return False

list1 = LinkedList(1, LinkedList(2, LinkedList(3)))
list2 = LinkedList(1, LinkedList(2, LinkedList(3)))

# Test the cntn_link function
print(cntn_link(list1, 2))
print(cntn_link(list2, 4))