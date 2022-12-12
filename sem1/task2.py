# 2. Напишите программу, которая на вход принимает 
# 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


a = int(input('vvedite 4islo: '))
i = 0
max = a
while i < 4:
    s = int(input('vvedite 4islo: '))
    if max < s:
        max = s
    i = i + 1
print(max)


# через массив
# import array

# arr = []
# for i in range(5):
#     arr.append(int(input(f"Введите число {i+1}: ")))
# max = arr[0];
# for i in range(1,5):
#     if arr[i]>max:1
#         max = arr[i]    
# print(max)
#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# a = int(input())
# b = int(input())
# if a**2==b or b**2==a:
#     print("yes")
# else:
#     print("no")
# #Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# # print(max(int(input()),int(input()),int(input())))
# a = int(input())
# maxx = a
# for i in range(4):
#     a = int(input())
#     if a>maxx:
#         maxx = a
# print(maxx)