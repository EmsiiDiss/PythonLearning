#dzialanaia na napisach
a = "AlA mA kOta"

print(a+a, a*3, sep="\n")

print(f"{a =}",
      f"{a.upper()=}", 
      f"{a.lower()=}", 
      f"{a.title()=}",
      f"{a.capitalize()=}",
      f"{a.replace("D","9")=}",
      f"{a.isnumeric()=}",
      f"{"1234".isnumeric()=}",
      f"{a.count("A") = }", 
      sep="\n")

print(a.lower().upper().count("D"))

print(a.startswith("Ala"), a.endswith("kota"))

print(a, a.split())
s1 = "apple, banana, pear"
fruits = s1.split(", ")

print(": ".join(fruits))

s = "ABCDEFGHIJKMNOPRST"
print(s[0])
print(s[1])
print(len(s))
print(s[len(s) - 1])
print(s[-2])
print(s[5])
#print(s[20])   # powoduje błąd przez wilkość str

#Slices start:stop:step
print(s[3:8:3])
print(f"{s = } =",
      f'{s[:5]} =',
      f'{s[:20]} =',
      f'{s[5:10]} =',
      f'{s[::-1]}',
      f'{s[5::2]}',
      sep = "\n")

a = [1,24,5]
s = [43, 54, 21, 6575, 2354, "dsfgdg", "232", [324, 534, "xd322", "232"], a]
print(s[3:8:3])
print(f"{s = } =",
      f'{s[:5]} =',
      f'{s[:20]} =',
      f'{s[5:10]} =',
      f'{s[::-1]} =',
      f'{s[5::2]} =',
      sep = "\n")

print(s)
print(len(s))

a[2] = 354
print(a)
print(s)
g = "napis"
print(list(g))

s.append(546)
s.remove(21)
s.pop(5)
s.insert(0, 100)
print(s)

print(s.count((21)))
s.extend([543, 5345, "guih"])

print(s)

#bez użycia copy
a = [1, 2, 3]
b = a
a[1] = -1
print(a,b, a is b)
#lista a jest modyfikowana w tym samym co b


#z użyciem copy
a = [1, 2, 3]
b = a.copy()
a[1] = -1
print(a,b, a is b)
#lista a NIE jest modyfikowana w tym samym co b


fruits = ["apple", "banana", "orange", "Johny", "melon"]
for i in range(len(fruits)):
    print(i, fruits[i])

for i in range(len(fruits)):
    if fruits[i].endswith("e"):
        print(fruits[i]) 


for fruit in fruits:
    print(fruit)           

for i, fruit in enumerate(fruits):
    print(i, fruit)        

for i, fruit in enumerate(fruits, 10):
    print(i, fruit)                    


prices = [1.99, 3.99, 4.99, 7.623, 4.123, 3453.4235 , 0.0]

for price, fruit in zip(prices, fruits):
    print(f'{fruit} costs {price} zł')


for i, (price, fruit) in enumerate(zip(prices, fruits), 1):
    print(f'{i}. {fruit} costs {price} zł')

#krotki

a = (1,2,5,6,9)
print(a)
print(a[4])
print(len(a))
#a[2] = -1 -> błąd, KROTKI NIE SĄ MODEFIKOWALNE

b = [10, 20, 30]
c = tuple(b)
d = list(c)
print(b, c, d)



a = 2           #int
b = 2,          #krotka
b2 = 2.         #float
c = (2)         #int
d = (2,)        #krotka
print(type(a), type(b), type(b2), type(c), type(d))

#zbiory
a = {1,2,4,78,3,24,21,57,79,21,1,2,3,5}
print(a)
# print(a[0]) nie można
a.add(100)
a.remove(2)
print(a)
print(set(a))
c = list(a)
print(c)


a = {1,2,3}
b = {3,5,6}
print(f'{a.intersection(b) = }',
      f'{a.difference(b) = }',
      f'{a.symmetric_difference(b) = }',
      f'{a.union(b) = }',
      sep="\n")


a = {}          #słownik
b = set()       #set
print(type(a), type(b))

a = {}
a[5] = "napis"
a["klucz"] = "wartosc"
a['k3'] = 10
print(a)

a.pop(5)
del a['k3']
print(a)

print(len(a))

# print(a[0]) KeyError brak elem

print(a.get(0, "Wartość domyślna"))
print(a.get('klucz', "Wartość domyślna"))


fruits = {
    'apple': 1.99,
    'lemon': 234.21,
    'fsd': 32.89
}

print(fruits)