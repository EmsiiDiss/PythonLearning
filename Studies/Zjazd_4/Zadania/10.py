print("Podaj x1, y1, x2 oraz y2")
x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))

x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))

x = abs(x1 - x2)
y = abs(y1 - y2)

pole = x*y
obwod = 2 * x + 2 * y

print(f'Pole: {pole}' 
      f'Obwód: {obwod}', 
      sep='\n')


