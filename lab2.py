from random import randint
# функция с заданием
def task():
    print("Вариант №6. Выполнила студентка группы 6101-090301D Горбунцова А.А.\n"
          "Задание: \n"
          "1. В списке целочисленных элементов найти максимальный ненулевой элемент\n"
          "2. С использованием цикла while найти в списке индекс первого отрицательного четного элемента\n"
          "3. Отсортировать список (без использования стандартных функций сортировки) по убыванию младших цифр "
          "элементов списка (сортировка Шелла)\n\n"
          "Введите способ заполнения списка:\n"
          "1 - ввод элементов списка в одну строку через пробел:\n"
          "любое число - автоматическое формирование списка из n элементов: ")
# получение рандомного массива
def random_array(botton, upper, number):
    user_array = [randint(botton, upper) for i in range(number)]
    return user_array
# функция поиска максимального ненулевого элемента
def max_nonzero(array):
    min_el = -10 ** 10
    for i in range(0,len(array)):
        if array[i] != 0 and array[i] > min_el:
            min_el = array[i]
    return min_el
# функция поиска индекса первого отрицательного четного элемента
def search_index(array):
    i = 0
    while (i < len(array) and ((array[i] % 2 != 0) or (array[i] >= 0))):
        i += 1
    return i
# функция поиска младшей цифры
def min_fig(element):
    element %= 10

    return element
# функция сортировки
def shell_sort(lst):
    step_len = len(lst) // 2
    while step_len > 0:
        for index in range(step_len, len(lst)):
            cur_val = abs(lst[index])
            cur_it = index
            while cur_it >= step_len and (min_fig(abs(lst[cur_it - step_len])) < min_fig(abs(cur_val))):
                lst[cur_it] = lst[cur_it - step_len]
                cur_it -= step_len
                lst[cur_it] = cur_val
        step_len //= 2
    return lst
# main
task()
user_answer = int(input())
user_array = []
if user_answer == 1:
    user_array = list(map(int, input("Введите в строку элементы списка: ").split()))
    print("Введенный список:\n", user_array)
else:
    number_elements = int(input("Введите количество элементов в списке: "))
    bottom_line = int(input("Введите нижнюю границу: "))
    upper_bound = int(input("Введите верхнюю границу: "))
    user_array = random_array(bottom_line, upper_bound, number_elements)
    print("Сгенерированный список:\n", user_array)

max_non_zero = max_nonzero(user_array)
first_index = search_index(user_array)
if max_non_zero != -10 ** 10:
    print("максимальный ненулевой элемент: ", max_non_zero)
else:
    print("Все элементы списка нулевые")
if first_index < len(user_array):
    print("индекс первого отрицательного четного элемента: ", first_index)
else:
    print("В данном списке не существует отрицательного четного элемента")
print("Исходный список: \n", user_array)
print("Отсортированный список \n",shell_sort(user_array))