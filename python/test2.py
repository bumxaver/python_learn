l=[3,6,7,4,-5,4,3,-1]
print(sum(l))

if sum(l)>2:
    print(len(l))
else:
    print('nothing')

print(min(l),max(l))
b=min(l)-max(l)
if abs(b)>10:
    print(sorted(l))
else:
    print('Разность больше или равно 10')