class link_list:
    def __init__(self, item, next_item=None):
        self.item = item
        self.next_item = next_item

    def __repr__(self):
        if self.next_item is None:
            return f'[{self.item}]'
        return f'[{self.item}, {self.next_item}]'
def link(item, next_item=None):
    return link_list(item, next_item)


def apnd(lnk, m):
    new_item = link(m)
    if lnk is None:
        return new_item

    current = lnk
    while current.next_item:
        current = current.next_item
    current.next_item = new_item
    return lnk
def first(lst):
    return lst.item


def rest(lst):
    return lst.next_item
l = link(1, link(2, link(3)))
n = apnd(l, 4)
print(first(rest(rest(rest(n)))))