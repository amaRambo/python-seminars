# Имеется список id сотрудников из 10 элементов, 
# каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda
import random

id = [ random.randint(1,100) for i in range (10)]
print(id)
users = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10"]
res = list(zip(id,users))
print(res)
res = sorted(res, key = lambda x: x[0])
print(res)

res2 = list(filter(lambda x: not x[0]%2==0, res))
print(res2)
for el in res2:
    print(el[1])
