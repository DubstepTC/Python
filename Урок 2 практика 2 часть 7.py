a = int(input("Введите число 1 : "))
b = int(input("Введите число 2 : "))
c = int(input("Введите число 3 : "))
if (a==b and a==c):
    print(3)
elif ((b==a and b!=c) or (b==c and a!=c) or (c==a and b!=c)):
    print(2)
else:
    print(0)
