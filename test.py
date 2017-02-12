from itertools import groupby

class A(object):

    def __init__(self, b, c):
        self.b = b
        self.c = c


items = [A(1, 2), A(1, 2), A(1, 2), A(2, 2), A(3, 4), A(3, 4), A(5, 6)]

groups = groupby(items, lambda a: (a.c))


ls =[]
for key, group in groups:
    temp = len(list(group))
    print "Key: %s, Number of items: %s " % (key, temp )
    ls.append(temp)
print sorted(ls)
