# Selection sort
#
# Time: O(n^2)


# p, r - don't need them here. They are for quick sort.
def selection_sort(array, p=None, r=None):
    array_length = len(array)

    for i in range(0, array_length - 1):
        smallest = i

        for j in range(i + 1, array_length):
            if array[j] < array[smallest]:
                smallest = j

        array[i], array[smallest] = array[smallest], array[i]

    return array
