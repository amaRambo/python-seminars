# 20. Задайте список. Напишите программу, 
# которая определит, присутствует ли в 
# заданном списке строк некое число.

a = ['123', 'dasd', 'qweqwe']
flag = False
for i in a:
    if i.isdigit():
        flag = True
        break
print(flag)

# for i in a:
#     if type(a[i]) == int:
#         print("+")
#     else:
#         print("-")