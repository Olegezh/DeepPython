# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 10

# print(num)

while count > 0:
    user_num = int(input("введите целое число  У вас {} попыток: ".format(count)))
    if num > user_num:
        print("загаданое число больше чем ", user_num)
    elif num < user_num:
        print("загаданое число меньше чем ", user_num)
    else:
        print("верно")
        quit()
    count -= 1

print("попытки за кончились")
