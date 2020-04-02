# Insertion sort
#
# Time: O(n^2)


# p, r - don't need them here. They are for quick sort.
def insertion_sort(array, p=None, r=None):
    array_length = len(array)

    for i in range(1, array_length):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    return array
