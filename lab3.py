import os.path


def task():
    print(f"Лабораторная работа №3\nВариант №6. Выполнила студентка группы 6101-090301D Горбунцова А.А\nЗадание: "
          f"написать программу, которая для каждой строки исходного файла будет выводить в результирующий файл "
          f"последовательность цифр\n('0','1'..'9') из входной последовательности и, через пробел, частот их "
          f"повторения. Печать должна происходить в порядке возрастания.\n")


def strToRes(s):
    a = [0] * 10
    for i in range(len(s)):
        if ord(s[i]) in range(48, 58):
            a[ord(s[i]) - ord("0")] += 1
    res = ""
    for c in range(10):
        if a[c] > 0:
            res = res + str(chr(ord("0") + c)) + " - " + str(a[c]) + ", "
    res = res[0:len(res) -2 ]
    return res


def fileToFile(fname1, fname2):
    f1 = open(fname1, "r")
    f2 = open(fname2, "w")
    data = f1.readlines()
    for s in data:
        res = ""
        if s != "":
            s = s.upper()
            res = strToRes(s)
            f2.write(res + "\n")
    f1.close()
    f2.close()

task()
filename1 = input("Введите имя исходного файла: ")
if os.path.exists(filename1):
    filename2 = input("Введите имя результирующего файла: ")
    fileToFile(filename1, filename2)
    print("Задание выполнено")
else:
    print("Такого файла не существует")
