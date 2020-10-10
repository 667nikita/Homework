a = tuple(input('>>>'))
b = {x: a.count(x) for x in set(a)}
c = [x for x in b.keys() if b[x] == max(b.values())]
print(c)

