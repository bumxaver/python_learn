#Переводит UNIX-timestamp в человекочитаемый формат

import arrow

while True:
    a=input()

    print(arrow.get(a))
