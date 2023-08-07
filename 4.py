class LinkedList:
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item

def srt(lnk):
    if lnk is None or lnk.next_item is None:
        return True
    current = lnk
    while current.next_item:
        if current.item > current.next_item.item:
            return False
        current = current.next_item

    return True

def link(item, next_item=None):
    return LinkedList(item, next_item)


def empty():
    return None
lnk1 = link(1, link(2, link(3, link(4, empty()))))
lnk2 = link(1, link(3, link(2, link(4, link(5, empty())))))
lnk3 = link(3, link(3, link(3, empty())))

print(srt(lnk1))
print(srt(lnk2))
print(srt(lnk3))
