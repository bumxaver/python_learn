#Дан список числовых значений, насчитывающий N элементов. Поменяйте местами
#первую и вторую половины списка.

a=[int(input()) for i in range(int(input()))]
print(a)
s=(len(a)/2)

print(list(a[int(s):])+list(a[:int(s)]))


