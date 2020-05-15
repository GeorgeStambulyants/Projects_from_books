from binary_search import binary_search
from recursive_binary_search import recursive_binary_search

def test_binary_search(search_func):
    array = list(range(10))
    x_1 = 3
    index_x_1 = array.index(x_1)
    print('testcase #1: ', end='')
    if search_func(array, x_1) == index_x_1:
        print('OK')
    else:
        print('FAIL')

    x_2 = 9
    index_x_2 = array.index(x_2)
    print('testcase #2: ', end='')
    if search_func(array, x_2) == index_x_2:
        print('OK')
    else:
        print('FAIL')

    x_3 = 0
    index_x_3 = array.index(x_3)
    print('testcase #3: ', end='')
    if search_func(array, x_3) == index_x_3:
        print('OK')
    else:
        print('FAIL')

    x_4 = 11
    index_x_4 = None
    print('testcase #4: ', end='')
    if search_func(array, x_4) == index_x_4:
        print('OK')
    else:
        print('FAIL')


def test_recursive_binary_search(search_func):
    array = list(range(10))
    p = 0
    r = len(array) - 1
    x_1 = 3
    index_x_1 = array.index(x_1)
    print('testcase #1: ', end='')
    if search_func(array, p, r, x_1) == index_x_1:
        print('OK')
    else:
        print('FAIL')

    x_2 = 9
    index_x_2 = array.index(x_2)
    print('testcase #2: ', end='')
    if search_func(array, p, r, x_2) == index_x_2:
        print('OK')
    else:
        print('FAIL')

    x_3 = 0
    index_x_3 = array.index(x_3)
    print('testcase #3: ', end='')
    if search_func(array, p, r, x_3) == index_x_3:
        print('OK')
    else:
        print('FAIL')

    x_4 = 11
    index_x_4 = None
    print('testcase #4: ', end='')
    if search_func(array, p, r, x_4) == index_x_4:
        print('OK')
    else:
        print('FAIL')


print('Binary Search test')
test_binary_search(binary_search)

print('Recursive Binary Search test')
test_recursive_binary_search(recursive_binary_search)
