import random
import sys

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def test_sorting_functions(func):
    p = 0
    array_1 = list(range(20))
    sorted_array_1 = array_1[:]
    random.shuffle(array_1)
    print('testcase #1: ', end='')

    r = len(array_1) - 1
    func(array_1, p, r)
    if array_1 == sorted_array_1:
        print('OK')
    else:
        print('FAIL')

    array_2 = []
    sorted_array_2 = array_2[:]

    print('testcase #2: ', end='')

    r = len(array_2) - 1
    func(array_2, p, r)
    if array_2 == sorted_array_2:
        print('OK')
    else:
        print('FAIL')

    array_3 = [4]
    sorted_array_3 = array_3[:]

    print('testcase #3: ', end='')

    r = len(array_3) - 1
    func(array_3, p, r)
    if array_3 == sorted_array_3:
        print('OK')
    else:
        print('FAIL')

    array_4 = list(range(4, 30, 3))
    sorted_array_4 = array_4[:]
    random.shuffle(array_4)

    print('testcase #4: ', end='')

    r = len(array_4) - 1
    func(array_4, p, r)
    if array_4 == sorted_array_4:
        print('OK')
    else:
        print('FAIL')

    array_5 = [1, 1, 1, 1, 3, 3, 3, 4, 4, 0, 0, 0]
    sorted_array_5 = sorted(array_5[:])
    random.shuffle(array_5)

    print('testcase #5: ', end='')

    r = len(array_5) - 1
    func(array_5, p, r)
    if array_5 == sorted_array_5:
        print('OK')
    else:
        print('FAIL')

    array_6 = list(range(20))
    sorted_array_6 = array_6[:]

    print('testcase #6: ', end='')

    r = len(array_6) - 1
    func(array_6, p, r)
    if array_6 == sorted_array_6:
        print('OK')
    else:
        print('FAIL')

    array_7 = list(range(-10, 10))
    sorted_array_7 = sorted(array_7[:])
    random.shuffle(array_7)

    print('testcase #7: ', end='')

    r = len(array_7) - 1
    func(array_7, p, r)
    if array_7 == sorted_array_7:
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    print('Selection sort:')
    test_sorting_functions(selection_sort)
    print('---------------')

    print('Insertion sort:')
    test_sorting_functions(insertion_sort)
    print('---------------')

    print('Merge sort:')
    test_sorting_functions(merge_sort)
    print('---------------')

    print('Quick sort:')
    test_sorting_functions(quick_sort)
