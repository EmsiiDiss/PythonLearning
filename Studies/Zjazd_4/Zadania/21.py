import math

a = float(input('Wprowadź a'))
b = float(input('Wprowadź b'))
c = float(input('Wprowadź c'))
delta = b**2 - 4*a*c
print(delta)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Rozwiązania równania kwadratowego:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Równanie kwadratowe ma jedno rozwiązanie:")
    print("x =", x)
else:
    print("Równanie kwadratowe nie ma rzeczywistych rozwiązań.")


