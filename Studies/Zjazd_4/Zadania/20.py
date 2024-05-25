while True:
    a = input("Wpsiz działanie: ")
    
    if "+" in a:
        a = a.split(sep="+")
        wynik = int(a[0]) + int(a[1])
    elif "-" in a:
        a = a.split(sep="-")
        wynik = int(a[0]) - int(a[1])   
    elif "*" in a:
        a = a.split(sep="*")
        wynik = int(a[0]) * int(a[1])        
    elif "/" in a:
        a = a.split(sep="/")
        if int(a[1]) == 0:
            print("Dzielenie przez ZERO!")
            continue
        wynik = int(a[0]) / int(a[1])  
    print(wynik)
