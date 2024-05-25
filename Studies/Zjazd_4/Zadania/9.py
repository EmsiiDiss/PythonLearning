a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))


if (a + b) > c and (a + c) > b and (c + b) > a:
    print(f'Jest możliwość uworzenia trójkąta z boków {a}, {b} oraz {c}')

else:
    print(f'NIE ma możliwości uworzenia trójkąta z boków {a}, {b} oraz {c}')