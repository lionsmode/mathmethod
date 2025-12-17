"""
x = int(input("введите значение x:"))
y = int(input("введите значение y:"))
if (1 <= x <= 8) and (1 <= y <=8):
    if (x + y) % 2:
        print("белый")
    else:
        print("черный")
  """
  
 #zadacha 1

x1 = int(input("x1"))
x2 = int(input("x2"))
y1 = int(input("y1"))
y2 = int(input("y2"))

if 1 <= x1 <= 8 and 1 <= y1 <=8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("да")
    else:
        print("нет")
else:
    print("ошибка")
#zadacha 2
"""
k = int(input("введите значение k:"))
n = int(input("введите значение n:"))
sumi = 0
for i in range(k, n + 1):
    if i % 2 == 0:
        sumi += i
print("сумма", sumi)
"""

#zadacha 3
"""
sumi = 0
while True:
    chislo = int(input("введите число:"))
    if chislo == 0:
        break
    sumi += chislo
print("сумма", sumi)
"""

#zadacha 4
"""
n = int(input("введите число:"))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
"""
