import random

print("Из этих слов компьютер выбрал рандомное слово и рандомную букву из этого слова. Угадай")
l=['самовар ','весна','лето']
print(l)

x=random.choice(l)
y=random.choice(x)

print(x.replace(y,'?'))
print('Нажмите букву ')
#i=input()
#while i!=y:


while True:
    #print("Это слово:" + x.)
    i = input()
    if i!=y:
         print("Попробуйте еще раз")


    else:
        print("Угадали")
        break
