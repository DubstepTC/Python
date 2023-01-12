n = int(input("Введите кол-во минут: "))
chas = n // 60
minut = n % 60
if (chas > 23):
    chas = chas - 23
print ('Часов: ' + str(chas) + ' минут: ' + str(minut))

