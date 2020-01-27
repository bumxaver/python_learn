a=[int(input()) for i in range(int(input()))]
s=(len(a)/2)

print(list(a[int(s):])+list(a[:int(s)]))
