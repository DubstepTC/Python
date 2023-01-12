print("Пункт1")
a = int(input("Введите число 1 : "))
b = int(input("Введите число 2 : "))
print("Пункт2 четность нечетность")
if (a % 2 == 0  and b % 2 ==0):
    print("Числа четные")
    print("Условие четности - True"  )
    print("Условие нечетности - False")
elif ( a % 2 != 0 and b % 2 != 0):
    print("Числа нечетные")
    print("Условие четности - False")
    print("Условие нечетности - True")
print("Пункт3 сравнение чисел с 25 ")
if ( a == 25 or b == 25):
    print("Одно из чисел равно 25")
    print("Условие равенства хотя бы одного числа с 25 - True")
    print("Условие неравенства хотя бы одного числа с 25 - False")
elif( a != 25 or b != 25):
    print("Хотя бы одно число не равно 25")
    print("Условие неравенства хотя бы одного числа с 25 - True")
print("Пункт4")
stroka = "Hello"
stroka2 = str(input())
if (stroka == stroka2 ):
    print("Пользователь написал Hello")
    print("Условие ввода Hello - True")
    print("Условие ввода не Hello - False")
elif (stroka != stroka2):
    print("Пользователь не написал Hello")
    print("Условие ввода Hello - False")
    print("Условие ввода не Hello - True")