import random
print("Компьютер загадал число. Угадайте его")
print("Выход, чтобы выйти")
s=random.randint(0,30)

while True:
    a=input()
    if a.isalpha() and a != "Выход":
        print("wat")
        break
    elif a=="Выход":
        print("До свиданья")
        break
    else: #a.isalpha()==False:
        a=int(a)
        if int(a)>s:
            print("Это число меньше того, что было введено")
        elif int(a)<s:
            print("Это число больше того, что было введено")
        elif int(a)==s:
            print("Вы угадали")
            break
