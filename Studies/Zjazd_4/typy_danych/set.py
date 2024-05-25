print('=' * 50)
a = {1, 2, 3, 1, 3, 2, 4, 2, 1}  # set
print(a)
# print(a[0]) # Set nie jest uporządkowany
a.add(6)
a.remove(2)
print(a)

b = [1, 1, 2, 5, 5, 4, 3, 2, 1]
c = list(set(b))
print(c)

a = {1, 2, 3}
b = {3, 4, 5}
print(f'{a.intersection(b) = }',
      f'{a.difference(b) = }',
      f'{a.symmetric_difference(b) = }',
      f'{a.union(b) = }',
      sep='\n')