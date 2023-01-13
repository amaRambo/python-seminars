# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.

lst = [90, 88, 1, 6, 0, 100]
lst2 = []
for i in range(1,len(lst)-1):
    if lst[i+1] > lst[i] or lst[i-1] < lst[i]:
        lst2.append(lst[i])


# print(lst2)

# def posled(data):
#     result = []
#     flag = False
#     length=len(data)
#     for i in range(length-1):
#         for j in range(i+1,length):
#             if data[j]>data[i]:
#                 flag = True
#                 begin = i
#                 next = j
#                 break
#         if flag:
#             break
#     if flag: 
#         result.append(data[begin])
#         result.append(data[next])
#         for i in range(next+1,length):
#             if data[i]>result[-1]:
#                 result.append(data[i])
#         return result
#     else:
#         return -1






# data = [7, 5, 2, 3, 4, 6, 1, 7]
# data_posled = posled(data)
# print(data_posled)
