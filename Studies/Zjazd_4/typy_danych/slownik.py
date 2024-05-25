print('=' * 50)
a = {}
a[5] = 'napis'
a['klucz'] = 'wartość'
a['k3'] = 10
print(a)
print(a['k3'])

a.pop(5)
del a['k3']

print(a)
print(len(a))

# print(a[0]) # Błąd KeyError
print(a.get(0))
print(a.get(0, 'Wartość domyślna'))
print(a.get('klucz', 'Wartość domyślna'))

print('=' * 50)
fruits = {
    'apple': 1.99,
    'lemon': 3.55,
    'melon': 10.99,
    'orange': 2.44,
    'pear': 3.00,
}
print(fruits)

print('=' * 50)
for key in fruits:
    print(key, fruits[key])

print('=' * 50)
for key, value in fruits.items():
    print(key, value)

print('=' * 50)
for key in fruits.keys():
    print(key, fruits[key])

print('=' * 50)
for value in fruits.values():
    print(value)

print('=' * 50)
for i, (key, value) in enumerate(fruits.items(), 1):
    print(i, key, value)