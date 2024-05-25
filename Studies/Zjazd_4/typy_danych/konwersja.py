b = [10, 20, 30]
c = tuple(b)
d = list(c)
print(b, c, d)


a = 2     # int
b = 2,    # tuple
c = (2)   # int
d = (2,)  # tuple
print(type(a), type(b), type(c), type(d))

b = [1, 1, 2, 5, 5, 4, 3, 2, 1]
c = list(set(b))
print(c)

a = {}
b = set()
print(type(a), type(b))