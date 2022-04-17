


# int_list = []
# for element in input("ведите любые целые числа в любом количестве через пробел.").split():
#     int_list.append(int(element))
# s = sorted(int_list)
# print(s)


s = "5 6 11 13 2 3 14 1 9 15 10 8 7 6"
n = (sorted(list(map(int, s.split()))))
print(n)
M = max(n)
V = min(n)



def get_01 ():
    while True:
        get_1 = input('Введите целое положительное число в пределах списка: ')  # Ввод числа
        if get_1.isdigit():
            return get_1
A = int(get_01())


def get_2 (n, A):
    for i in range(len(n)):
        if A >= n[i] and A <= n[i + 1]:
            return i


if V > A:
    print(" Введено число меньше минимального списка")
    A = int(get_01())
elif V == A:
    print("Введено число равное минимальному в списке")

elif M == A:
    print("введено число равное максимальному в списке")
elif V < A < M:
    print("Введено число в пределах списка ")

elif A > M:
    print("Введено число больше максимального в списке ")
    A = int(get_01())

position = get_2(n, A)

print("нидекс= ", position)




