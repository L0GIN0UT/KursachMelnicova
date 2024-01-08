import time
from Menu import *
from Generate import *
from Sort import *
import os


def show_all(cameras):
    for camera in cameras:
        print()
        print("Фирма фотоаппарата: " + camera[0])
        print("Объектив: " + camera[1])
        print("Фирма объектива: " + camera[2])
        print("Жанр или направление съемки: " + camera[3])
        print("Место проведения: " + camera[4])
        if camera[4] == "на улице":
            print("Погодные условия: " + camera[5])
            print("Время съемки: " + camera[6])
        elif camera[4] == "в помещении":
            print("Количество света: " + camera[5])
        print()


def choice_of_person(choice, rest):
    print()
    if choice == 1:
        clear()
        menuForFirm1()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByFirmOfCamera1(a, rest)
        else:
            clear()
            menuForFirm2()
            time_freeze()
            a = check_input()
            if a < 11:
                rest = sortByFirmOfCamera2(a, rest)
            else:
                clear()
                menuForFirm3()
                time_freeze()
                rest = sortByFirmOfCamera3(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 2:
        clear()
        menuForLenses1()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByLenses1(a, rest)
        else:
            clear()
            menuForLenses2()
            time_freeze()
            rest = sortByLenses2(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 3:
        clear()
        menuForFirm1()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByFirmOfLenses1(a, rest)
        else:
            clear()
            menuForFirm2()
            time_freeze()
            a = check_input()
            if a < 11:
                rest = sortByFirmOfLenses2(a, rest)
            else:
                clear()
                menuForFirm3()
                time_freeze()
                rest = sortByFirmOfLenses3(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 4:
        clear()
        menuForGenre1()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByGenre1(a, rest)
        else:
            clear()
            menuForGenre2()
            time_freeze()
            rest = sortByGenre2(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 5:
        clear()
        menuForPlace()
        time_freeze()
        rest = sortByPlace(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 6:
        clear()
        menuForWeather()
        time_freeze()
        rest = sortByWeather(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 7:
        clear()
        menuForTime()
        time_freeze()
        rest = sortByTime(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 8:
        clear()
        menuForAmountOfLight()
        time_freeze()
        rest = sortByAmountOfLight(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 9:
        clear()
        rest = Restart()
        print("Характеристики были сброшены")
        time_freeze()
        return rest
    elif choice == 10:
        time_freeze()
        if check_res(rest):
            show_all(rest)
    elif choice == 11:
        exit()


def check_input():
    while True:
        a = input("Введите ваш ответ -> ")
        if a.isdigit():
            return int(a)


def check_res(rest):
    if len(rest) == 0:
        print()
        print("Приносим свои извинения")
        print("Но на данный момент наше приложение")
        print("Не может подобрать подходящие съемки по вашим предпочтениям")
        print("Попробуйте сбросить характеристики и выбрать другие критерии")
        print()
        time.sleep(2)
    else:
        return rest


def main(gen_rest):
    print("Подбор съемки \nАвтор: Анна Мельникова")
    rest = gen_rest
    while True:
        time_freeze()
        clear()
        print()
        menu()
        rest = choice_of_person(check_input(), rest)


def time_freeze():
    time.sleep(1)


def clear():
    print('\n'*80)


res = Restart()
main(res)
