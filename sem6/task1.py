# list comprehension

# a = [i for i in range(1,10)]    после можно добавить условие
#      |тут можно вставить рандом вместо i
# print(a)


# enumerate 

# a = [2, 4, 6, 8]
# for indx,val in enumerate(a):
#     if val > 5:
#         a[indx] = 0
# print(a)


# zip

# a = [1,2,3,4,5,6]
# months = ["june", "juli", "3", "4", "5", "6"]
# dit_s = {1:"ddd", 2:"112"}
# result = list(zip(a, months, dit_s))
# print(result[1][1])


# lambda

# summ = lambda a,b: a +b if a>5 else 0
# print(summ(7,3))


# map

# a = [2,4,6,8]
# a = list(map(lambda x: x*x, a))
# print(a)


#  filter - может применится к одному агрументу, тут х - это сам кортеж

# a = [1,2,3,4,5,6,7,8]
# def sorting(x):
#     if x%2==0:
#         return True
# res = list(filter(sorting, a))
# res = list(filter(lambda x:x%2, a)) - альтернатива
# print(res)


# sorted

# a = [(2,4,6), (4,5,6), (1,2,3)]
# res = sorted(a, key = lambda x: (x[2],x[1]))
# print(res)