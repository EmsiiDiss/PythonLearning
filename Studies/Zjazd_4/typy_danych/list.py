
a = [10, 20, 30, 40]
print(len(a))
print(a[0])
print(a[-1])
print(a[1:3])

b = [3, 9.4, 'Napis', a]
print(b)

a[2] = -3
print(a)
print(b)

s = 'napis'
print(list(s))

print('=' * 50)
a = [10, 20, 30, 40]

print(a)

a.append(50)  # Dodaj element do listy
print(a)

a.remove(40)  # Usuń pierwszy element o wartości 40
print(a)

a.pop(0)  # Usuń element z indeksu 0
print(a)

a.insert(0, 100)
print(a)

print(a.count(30))

print(a.index(30))

a.extend([60, 70, 80])
print(a)

print('=' * 50)

a = [1, 2, 3]
# b = a # Domyślnie nie jest robiona kopia!
b = a.copy()
a[1] = -1
print(a, b, a is b)

print('=' * 50)
fruits = ['apple', 'orange', 'lemon', 'pear', 'melon']

for i in range(len(fruits)):
    print(i, fruits[i])

print('=' * 50)
for i in range(len(fruits)):
    if fruits[i].endswith('e'):
        print(fruits[i])

print('=' * 50)
for fruit in fruits:
    print(fruit)

print('=' * 50)
for i, fruit in enumerate(fruits):
    print(i, fruit)

print('=' * 50)
for i, fruit in enumerate(fruits, 10):
    print(i, fruit)

print('=' * 50)
prices = [1.99, 3.99, 3.50, 4.60, 10.99]
for price, fruit in zip(prices, fruits):
    print(f'{fruit} costs {price} zł.')

print('=' * 50)
prices = [1.99, 3.99, 3.50, 4.60, 10.99]
for i, (price, fruit) in enumerate(zip(prices, fruits), 1):
    print(f'{i}. {fruit} costs {price} zł.')