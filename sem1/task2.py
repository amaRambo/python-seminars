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
