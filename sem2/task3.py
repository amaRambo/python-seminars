# 13. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять количество 
# вхождений одной строки в другой.

stroka1 = input("ВВедите строку: ")
stroka2 = input("ВВедите строку: ")
count = 0 
for i in range(len(stroka1)):
    if stroka1[i:i+len(stroka2)]==stroka2:
        count +=1
print(count)
# print (one_str.count (two_str))