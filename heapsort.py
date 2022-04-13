# # Основной алгоритм сортировки кучей
# def HeapSort(data):
#     # Формируем первоначальное сортирующее дерево
#     # Для этого справа-налево перебираем элементы массива
#     # (у которых есть потомки) и делаем для каждого из них просейку
#     for start in range((len(data) - 2) // 2, -1, -1):
#         HeapSift(data, start, len(data) - 1)
#
#         # Первый элемент массива всегда соответствует корню сортирующего дерева
#     # и поэтому является максимумом для неотсортированной части массива.
#     for end in range(len(data) - 1, 0, -1):
#         # Меняем этот максимум местами с последним
#         # элементом неотсортированной части массива
#         data[end], data[0] = data[0], data[end]
#         # После обмена в корне сортирующего дерева немаксимальный элемент
#         # Восстанавливаем сортирующее дерево
#         # Просейка для неотсортированной части массива
#         HeapSift(data, 0, end - 1)
#     return data
#
#
# # Просейка свеху вниз, в результате которой восстанавливается сортирующее дерево
# def HeapSift(data, start, end):
#     # Начало подмассива - узел, с которого начинаем просейку вниз
#     root = start
#
#     # Цикл просейки продолжается до тех пор,
#     # Пока встречаются потомки, большие чем их родитель
#     while True:
#
#         child = root * 2 + 1  # Левый потомок
#         # Левый потомок за пределами подмассива - завершаем просейку
#         if child > end: break
#
#         # Если правый потомок тоже в пределах подмассива,
#         # то среди обоих потомков выбираем наибольший
#         if child + 1 <= end and data[child] < data[child + 1]:
#             child += 1
#
#         # Если больший потомок больше корня, то меняем местами
#         # при этом больший потомок сам становится корнем,
#         # от которого дальше опускаемся вниз по дереву
#         if data[root] < data[child]:
#             data[root], data[child] = data[child], data[root]
#             root = child
#         else:
#             break
#
data = [5,6,11,13,2,3,14,1,9,15,6,10,8,7,12]
# print(HeapSort(data))

# сортировка Timsort  уже встроена в Python


print(sorted(data))

m = max(data)
M = int(m)

v = min(data)
V = int(v)


# int_list = []
# for element in input("ведите любые целые числа в любом количестве через пробел.").split():
#     int_list.append(int(element))
# aa = sorted(int_list)

# print(aa)
print(M)
print(V)
# > 1 word meow
# > ['1', 'word', 'meow']
# > <class 'list'>

# проверка числа на правильность введения

# def ok_num():
#
#     while num is None:
#         num = int(input("Введите номер комнаты: "))
#         room_numbe()
#         if V < num:
#             print(" Введено число меньше минимального списка")
#         elif V == num:
#             print("Введено число равное минимальному списка")
#
#         elif M < num:
#             print("Введен о число больше максимального в списке ")
#         elif M == num:
#             print("введено число равное максимальному в списке")
#
#         elif M > num > V:
#             print("Ввел хорошее число число")
#
#
# def room_number():
#     while True:
#         try:
#             tmp = int(num)
#             return tmp
#         except ValueError:
#             print("Вы ввели не число. Повторите ввод")
#
# numba = room_number()
# #
# #
# #
# print(numba)
# ok_num(numba)

def getNumber02 ():
    while True:
        getNumber = input('Введите целое положительное число: ')  # Ввод числа
        if getNumber.isdigit() : return getNumber
        else:
            break

# print(getNumber02())
a = getNumber02()
A = int(a)
if V > A:
    print(" Введено число меньше минимального списка")
elif V == A:
    print("Введено число равное минимальному списка")

elif M < A:
    print("Введено число больше максимального в списке ")
elif M == A:
    print("введено число равное максимальному в списке")

elif M > A > V:
    print(" Ввел хорошее  число")


