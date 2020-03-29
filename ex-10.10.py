#Дана матрица (см. упражнение 10.10). Вывести номер строки, содержащей
#максимальное число одинаковых элементов.

import random

n=int(input())
m=int(input())
c=int()
sum=0
max=0
matr=[[random.randrange(0,9) for i in range(n)]for k in range(m)]


print(matr)
for q in matr:
    for l in q:
        if q.count(l)>max:
            max=q.count(l)
            c=matr.index(q)
        
print("Индекс с максимальным количеством повторяющихся чисел= "+ str(c))
