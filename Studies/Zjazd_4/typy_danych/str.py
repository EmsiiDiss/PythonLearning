#Napisy i operacje na nich

s = 'AbCdEfghijkl'
s = 'Ala ma kota'

print(s * 3)
print(s + s)

print(f'{s = }',
      f'{s.upper() = }',
      f'{s.lower() = }',
      f'{s.title() = }',
      f'{s.capitalize() = }',
      f'{s.replace("A", "a") = }',
      f'{s.isnumeric() = }',
      f'{"1234".isnumeric() = }',
      f'{s.count("A") = }',
      sep='\n')

print(s.lower().title().upper())
print(s.startswith('Ala'), s.endswith('kota'))

print(s, s.split())
s1 = 'apple, lemon, pear'
print(s1.split(', '))

fruits = s1.split(', ')
print('; '.join(fruits))

s = 'ABCDEFGHIJKLMNOP'
print(s[0])
print(s[1])
print(len(s))  # Długość napisu
print(s[len(s) - 1])
print(s[-1])
print(s[-2])
print(s[5])
# print(s[20])  # Ten wiersz wywołuje błąd IndexError

# Slices start:stop:step
print(
    f'{s = }',
    f'{s[:5] = }',
    f'{s[:20] = }',
    f'{s[5:10] = }',
    f'{s[5:] = }',
    f'{s[:10:2] = }',
    f'{s[::-1] = }',
    f'{s[5::2] = }',
    sep='\n'
)