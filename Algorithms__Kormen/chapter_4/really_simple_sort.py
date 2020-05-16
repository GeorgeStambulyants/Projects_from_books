# This function sorts arrays that only contain 1 and 2
#
# Time: O(n)
import random


def really_simple_sort(arr):
    k = 0

    for i in arr:
        if i == 1:
            k += 1

    for i in range(k):
        arr[i] = 1
    for i in range(k, len(arr)):
        arr[i] = 2


def test_really_simple_sort(func):
    array_1 = [1] * random.randint(0, 10) + [2] * random.randint(0, 10)
    sorted_array_1 = array_1[:]
    random.shuffle(array_1)

    print('testcase#1:', end='')
    func(array_1)
    if array_1 == sorted_array_1:
        print('OK')
    else:
        print('FAIL')

    array_2 = [1] * random.randint(0, 10)
    sorted_array_2 = array_2[:]
    random.shuffle(array_2)

    print('testcase#2:', end='')
    func(array_2)
    if array_2 == sorted_array_2:
        print('OK')
    else:
        print('FAIL')

    array_3 = [2] * random.randint(0, 10)
    sorted_array_3 = array_3[:]
    random.shuffle(array_3)

    print('testcase#3:', end='')
    func(array_3)
    if array_3 == sorted_array_3:
        print('OK')
    else:
        print('FAIL')

    array_4 = []
    sorted_array_4 = array_4[:]
    random.shuffle(array_4)

    print('testcase#4:', end='')
    func(array_4)
    if array_4 == sorted_array_4:
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    test_really_simple_sort(really_simple_sort)
