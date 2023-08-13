"""
Урок 4. Словари, множества и профилирование
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""


n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))

list_1 = [int(input("Введите элемент первого числового набора ")) for _ in range(n)]
list_2 = [int(input("Введите элемент второго числового набора ")) for _ in range(m)]


set_1 = set(list_1)
set_2 = set(list_2)

set_result = set_1.intersection(set_2)
list_result = list(set_result)
list_result.sort()

print(list_result)


"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
заданной во входном файле грядки.
"""

n = int(input("Введите количество кустов на грядке: "))
q_berries = [int(input("Введите количество ягод на каждом кусте по порядку ")) for _ in range(n)]

max_sum = 0
max_index = 0

for i in range(len(q_berries)):
    sum = q_berries[i - 2] + q_berries[i - 1] + q_berries[i]
    if sum > max_sum:
        max_sum = sum
        max_index = q_berries[i - 1]

print(f"Собирающий модуль должен быть у куста с количеством ягод: {max_index}.\nПри этом максимальное количество собранных ягод будет равно {max_sum}.")

