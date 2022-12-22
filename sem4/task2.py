# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
import math
a = int(input())
b = int(input())
c = int(input())
d = b*b - 4 *a*c
if (d == 0):
    x = -(b/(2*a))
    print(x)
elif (d > 0):
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(x1, x2)
else:
    print("net korney")
