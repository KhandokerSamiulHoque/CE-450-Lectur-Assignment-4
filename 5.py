class LinkedList:
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item
def sum_lnk(lnk, g):
    total = 0
    current = lnk
    while current:
        total += g(current.item)
        current = current.next_item
    return total

def link(item, next_item=None):
    return LinkedList(item, next_item)

def empty():
    return None

sqr = lambda x: x * x
dbl = lambda y: 2 * y

lnk1 = link(1, link(2, link(3, link(4, empty()))))
lnk2 = link(3, link(5, link(4, link(6, empty()))))

print(sum_lnk(lnk1, sqr))
print(sum_lnk(lnk2, dbl))
