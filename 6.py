def change(lnk, u, v):
    link_update = []
    element = []
    while lnk:
        if lnk[0] == u:
            element.append(v)
        else:
            element.append(lnk[0])
        lnk = lnk[1]

    index = len(element) - 1
    counter = index
    while counter >= 0:
        link_update = link(element[counter], link_update)
        counter -= 1
    return link_update


def link(item, next):
    return [item, next]


l = link(1, link(2, link(3, [])))
n = change(l, 3, 1)
print(n)

m = change(n, 1, 2)
print(m)

change(m, 5, 1)
print(m)