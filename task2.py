import math
import os

def help_list():
    print("Функция          |   Синтаксис       ")
    print("------------------------------------")
    print("Сложение         |   слож        ")
    print("Вычитание        |   выч         ")
    print("Умножение        |   умн         ")
    print("Деление          |   дел         ")
    print("Логарифм         |   лог         ")
    print("Степень          |   степень     ")
    print("Округление вниз  |   окр вниз    ")
    print("Округление вверх |   окр вверх   ")
    print("------------------------------------")


action = "ничего"
list_of_action = ["слож","выч","умн","дел","лог","степень","окр вниз","окр вверх"]
Check_state =True # Usually using to create inf loop - to check correct input
print("Введите 'помощь' - для вывода всех доступных функций")
while Check_state:
    print("Введите команду:")
    inp = input()
    if inp== "помощь":
        help_list()
        continue

    if inp in list_of_action:
        action = inp
        break


    print("Некорректная команда!") # incorrect command if code came to this line




a=0
b=0

while Check_state:
    try:
        if action in ("слож","выч","умн","дел","степень"):
            a=float(input("Введите первое число: "))
            break

        if action =="лог":
            a=float(input("Введите аргумент логарифма: "))
            if a<=0:
                print("Аргумент логарифма должен быть строго больше нуля!")
                continue
            break
        if action in ("окр вниз","окр вверх"):
            a=float(input("Введите число, что будет округлено: "))
            break
    except:
        print("Вы ввели некорректное число!")



while Check_state:
    try:
        if action in ("слож","выч","умн","дел","степень"):

            b=float(input("Введите второе число: "))
            if action == "дел":
                if b == 0:
                    print("Делить на ноль нельзя!")
                    continue
            break

        if action =="лог":
            b=float(input("Введите основание логарифма: "))
            if b==1 or b <=0:
                print("Основание логарифма должен быть строго больше нуля и не равно единице!")
                continue
            break
        if action in ("окр вниз","окр вверх"):
            b=float(input("Введите число, до какого знака будет округление: "))
            break
    except:
        print("Вы ввели некорректное число!")


if action == "слож":
    print(a + b)
elif action == "выч":
    print(a - b)
elif action == "умн":
    print(a * b)
elif action == "дел":
    print(a / b)
elif action == "лог":
    print(math.log(a, b))
elif action == "степень":
    print(a ** b)

elif action=="окр вниз":
    a=a*(10**b)
    a=math.floor(a)
    a=a/(10**b)
    print(a)
elif action == "окр вверх":
    a = a * (10 ** b)
    a = math.ceil(a)
    a = a / (10 ** b)
    print(a)