import random
import sys

from selection_sort import selection_sort


def test_sorting_functions(func):
    array_1 = list(range(20))
    sorted_array_1 = array_1[:]
    random.shuffle(array_1)

    print('testcase #1: ', end='')
    if func(array_1) == sorted_array_1:
        print('OK')
    else:
        print('FAIL')

    array_2 = []
    sorted_array_2 = array_2[:]

    print('testcase #2: ', end='')
    if func(array_2) == sorted_array_2:
        print('OK')
    else:
        print('FAIL')

    array_3 = [4]
    sorted_array_3 = array_3[:]

    print('testcase #3: ', end='')
    if func(array_3) == sorted_array_3:
        print('OK')
    else:
        print('FAIL')

    array_4 = list(range(4, 30, 3))
    sorted_array_4 = array_4[:]
    random.shuffle(array_4)

    print('testcase #4: ', end='')
    if func(array_4) == sorted_array_4:
        print('OK')
    else:
        print('FAIL')

    array_5 = [1, 1, 1, 1, 3, 3, 3, 4, 4, 0, 0, 0]
    sorted_array_5 = sorted(array_5[:])
    random.shuffle(array_5)

    print('testcase #5: ', end='')
    if func(array_5) == sorted_array_5:
        print('OK')
    else:
        print('FAIL')

    array_6 = list(range(20))
    sorted_array_6 = array_6[:]

    print('testcase #6: ', end='')
    if func(array_6) == sorted_array_6:
        print('OK')
    else:
        print('FAIL')

    array_7 = list(range(-10, 10))
    sorted_array_7 = sorted(array_7[:])
    random.shuffle(array_7)

    print('testcase #7: ', end='')
    if func(array_7) == sorted_array_7:
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    print('Selection sort:')
    test_sorting_functions(selection_sort)
    print()
