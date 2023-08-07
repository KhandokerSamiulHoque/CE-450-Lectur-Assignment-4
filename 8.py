def insrt(l, elm, ind):
    old = None
    new = l
    while new and ind > 0:
        old = new
        new = new[1]
        ind -= 1

    new_item = link(elm, new)
    if old is None:
        return new_item
    else:
        old[1] = new_item
    return l
def link(item, next):
    return [item, next]


l = link(11, link(12, link(13, [])))
n = insrt(l, 2021, 1)
print(n)
m = insrt(n, 2022, 20)
print(m)