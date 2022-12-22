# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
a = int(input())
b = int(input())
for i in range(a*b):
    if i%a == 0 and i%b == 0:
        print(i)
        break