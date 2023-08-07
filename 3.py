class LinkedList:
    def __init__(self, item, nxt=None):
        self.item = item
        self.nxt = nxt
    def __repr__(self):
        if self.nxt is None:
            return f'[{self.item}, [ ] ]'
        return f'[{self.item}, {self.nxt}]'

def rvrs_lnk(s):
    reversed_lst = None
    while s:
        reversed_lst = LinkedList(s.item, reversed_lst)
        s = s.nxt
    return reversed_lst

def lnk(node, nxt=None):
    return LinkedList(node, nxt)

def empty():
    return None
output = rvrs_lnk(lnk(1, lnk(2, lnk(3, lnk(4, empty())))))
print(output)