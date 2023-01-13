# Напишите программу, удаляющую из текста все слова, содержащие "абв".


lst = "фыва фыва ыва ывв пып кпук абвпоу"
a = lst.strip().split()
b = []
print(a)
l = len(a)
for i in range(l):
    if "абв" not in a[i]:
        b.append(a[i])
            


print(b)   
print(lst)
print(" ".join(b))