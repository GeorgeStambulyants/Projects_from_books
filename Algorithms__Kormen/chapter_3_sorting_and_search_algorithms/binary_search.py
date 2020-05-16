# Binary search
#
# Time: O(lg n)


def binary_search(array, x):
    '''
        array - sorted array, x - required element
        returns the index of required element or None
    '''
    # left and rigth borders of the subarray
    # Initially subaray is the whole array
    p = 0
    r = len(array) - 1
    while p <= r:
        q = (p + r) // 2

        if array[q] == x:
            return q
        elif array[q] > x:
            r = q - 1
        else:
            p = q + 1

    return None
