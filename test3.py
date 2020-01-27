s=int(input("Введите число: "))
b=0
for i in range(1,s+1):
    if i%2!=0:
        b+=i**2
    
print(b)

