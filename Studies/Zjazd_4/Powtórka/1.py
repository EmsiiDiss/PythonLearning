a = 3 #int
b = 3.5 #float
c = "Hello World" #str

print(a, b, c, "to są zmienne")

print(a, b, c, "to są zmienne", sep="_to_jest_separator_", end="_to_jest_koniec_\n")

print(a, b, c, "to są zmienne", sep="\n")

print(a+b, a-b, a*b, a/b)

print(f'{a=}, {b=}',f'{a+b=}, {a-b=}, {a*b=}', sep="\n")

a = int(input("Podaj loczbę: "))

print(a, a+2)