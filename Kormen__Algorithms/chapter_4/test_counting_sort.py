import random

from counting_sort import counting_sort


def test_counting_sort(func):
    array_1 = list(range(20))
    sorted_array_1 = array_1[:]
    random.shuffle(array_1)
    m1 = 20

    print('testcase #1: ', end='')

    if func(array_1, m1) == sorted_array_1:
        print('OK')
    else:
        print('FAIL')

    array_2 = []
    sorted_array_2 = array_2[:]
    m2 = 0

    print('testcase #2: ', end='')

    if func(array_2, m2) == sorted_array_2:
        print('OK')
    else:
        print('FAIL')

    array_3 = [4]
    sorted_array_3 = array_3[:]
    m3 = 5

    print('testcase #3: ', end='')

    if func(array_3, m3) == sorted_array_3:
        print('OK')
    else:
        print('FAIL')

    array_4 = list(range(4, 30, 3))
    sorted_array_4 = array_4[:]
    random.shuffle(array_4)
    m4 = 29

    print('testcase #4: ', end='')

    if func(array_4, m4) == sorted_array_4:
        print('OK')
    else:
        print('FAIL')

    array_5 = [1, 1, 1, 1, 3, 3, 3, 4, 4, 0, 0, 0]
    sorted_array_5 = sorted(array_5[:])
    random.shuffle(array_5)
    m5 = 5

    print('testcase #5: ', end='')
    
    if func(array_5, m5) == sorted_array_5:
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    test_counting_sort(counting_sort)
