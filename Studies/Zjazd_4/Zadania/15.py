n = 5
a = [3]
for i in range(n):
    an1 = a[-1]
    an = an1**2 - an1
    a.append(an)
print(a)