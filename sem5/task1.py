#  В файле находится N натуральных чисел, записанных 
#  через пробел. Среди чисел не хватает одного, 
#  чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

f = open("s5t1.txt","r")
s = f.readline()
lst =  s.strip().split()
for i in range(1,len(lst)):
    if int(lst[i]) - 1 != int(lst[i-1]):
        print(int(lst[i]) - 1)
        break