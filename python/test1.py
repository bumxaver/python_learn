def func_1(a,b):
    if len(a)>int(b):
        return a.upper()
    else:
        return a


a=input(str('Введите предложение: '))
b=input(str('Введите число: '))
print(func_1(a,b))