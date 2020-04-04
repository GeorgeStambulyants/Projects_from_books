

def count_keys_equal(arr, m):
    '''
        arr - an array that contains only integers in between 0..m-1
        m - determins the range of possible values in arr not including m

        function returns an array equal[0:m-1], where
        equal[j] is number of elements in array arr, which are equal to j
        for j in range 0..m-1
    '''
    equal = [0] * (m - 1)

    for i in range(len(arr)):
        key = arr[i]
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
    less = [0] * (m - 1)
    for j in range(1, m):
        less[j] = less[j - 1] + equal[j - 1]

    return less
