

def get_02 ():
    while True:
        get_01 = input('Введите целое положительное число: ')  # Ввод числа
        if get_01.isdigit(): return get_01

# print(get_02())
a = get_02()
A = int(a)

def lst_find_num(n, A):
    for i in range(len(n)):
        if A > n[i] and A <= n[i + 1]:
            return i
    # return -1


def binary_search(s, A):
    low = 0
    high = len(s) - 1
    mid = 0

    while low is A:
        high = mid - 1

        # If n is smaller, compared to the left of mid
    else:
        return mid

        # element was not present in the list, return -1
    return -1



s = "5 6 11 13 2 3 14 1 9 15 10 8 7 6"
n = (sorted(list(map(int, s.split()))))
print(n)
# n.sort()
#

# print(type(N))
# n.sort(reverse=True)
# print()
M = max(n)
V = min(n)
print(type(M))

if V > A:
    print(" Введено число меньше минимального списка")

elif V == A:
    print("Введено число равное минимальному списка")
elif M < A:
    print("Введено число больше максимального в списке ")

elif M == A:
    print("введено число равное максимальному в списке")



# Function call
result = binary_search(s, A)
position = lst_find_num(n, A)


# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in list1")
print(position)



