# Selection sort
#
# Time: O(n^2)


def selection_sort(array):
    array_length = len(array)

    for i in range(0, array_length - 1):
        smallest = i

        for j in range(i + 1, array_length):
            if array[j] < array[smallest]:
                smallest = j

        array[i], array[smallest] = array[smallest], array[i]

    return array
