"""
x = int(input("x: "))
y = int(input("y: "))
if x > 8 or y > 8 or x < 0 or y < 0:
    print("No")
elif (x+y) % 2 == 1:
    print("White")
elif (x+y) % 2 == 0:
    print("Black")
"""

#1
"""
kletka_start_x = int(input("start x: "))
kletka_start_y = int(input("start y: "))
kletka_end_x = int(input("end x: "))
kletka_end_y = int(input("end y: "))
if kletka_start_x > 8 or kletka_start_y > 8 or kletka_start_x < 0 or kletka_start_y < 0 or kletka_end_x > 8 or kletka_end_y > 8 or kletka_end_x < 0 or kletka_end_y < 0:
    print("Ошибка")
elif kletka_end_x - kletka_start_x == 1 and kletka_end_y - kletka_start_y == 2 or kletka_end_x - kletka_start_x == 2 and kletka_end_y - kletka_start_x == 1:
    print("Может за один ход")
else:
    print("Не может за один ход")
"""

#2
"""
chislo = int(input("N: "))
chislo2 = int(input("K: "))
summa = chislo + chislo2
for i in range(1, summa+1):
    if i % 2 == 0:
        print(i)
"""

#3
"""
n = 1
summa = 0
while n==1:
    vvod_chisla = int(input())
    summa += vvod_chisla
    if vvod_chisla == 0:
        print(summa)
        break
"""

#4
"""
factorial = 1
chislo = int(input())
for i in range(1, chislo+1):
    factorial *=i
print(factorial)"""