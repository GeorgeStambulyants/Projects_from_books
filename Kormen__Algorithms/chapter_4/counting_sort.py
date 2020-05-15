# Counting sort
#
#Time: O(n)


def count_keys_equal(A, m):
    '''
        A - an array that contains only integers in range(0, m)
        m - determins the range of possible values in A not including m

        function returns an array equal[0:m-1], where
        equal[j] is number of elements in array A, which are equal to j
        for j in range 0..m-1
    '''
    equal = [0] * m

    for i in range(len(A)):
        key = A[i]
        equal[key] += 1

    return equal


def count_keys_less(equal, m):
    '''
        equal - an array returned from count_keys_equal function.
        m - determins the range of indexes of the array equal - from 0 to m - 1

        function returns an array less[0:m-1], where
        each element less[j] for j in range(0, m) contains the
        following sum: equal[0] + equal[1] + ... + equal[j-1]
    '''
    less = [0] * m
    for j in range(1, m):
        less[j] = less[j - 1] + equal[j - 1]

    return less


def rearrange(A, less, m):
    '''
        A - an array that contains only integers in range(0, m)
        less - an array returned from function count_keys_less
        m - the range of values in array A

        this func returns array B which is sorted array A
    '''
    n = len(A)
    B = [0] * n

    for i in range(0, n):
        key = A[i]
        index = less[key]
        B[index] = A[i]
        less[key] += 1

    return B


def counting_sort(A, m):
    '''
        A - an array to sotr
        m - determins the range of possible values in A not including m

        returns sorted array
    '''
    equal = count_keys_equal(A, m)
    less = count_keys_less(equal, m)

    return rearrange(A, less, m)


def test_count_keys_equal_and_less_and_rearrange(func_equal, func_less, func_rearrange):
    arr = [4, 1, 5, 0, 1, 6, 5, 1, 5, 3]
    sorted_arr = sorted(arr)
    equal = [1, 3, 0, 1, 1, 3, 1]
    less = [0, 1, 4, 4, 5, 6, 9]
    m = 7

    print('test equal: ', end='')
    if func_equal(arr, m) == equal:
        print('OK')
    else:
        print('FAIL')

    print('test less: ', end='')
    if func_less(equal, m) == less:
        print('OK')
    else:
        print('FAIL')

    print('test rearrange: ', end='')
    if func_rearrange(arr, less, m) == sorted_arr:
        print('OK')
    else:
        print('FAIL')


if __name__ == '__main__':
    test_count_keys_equal_and_less_and_rearrange(
        count_keys_equal, count_keys_less, rearrange
    )
