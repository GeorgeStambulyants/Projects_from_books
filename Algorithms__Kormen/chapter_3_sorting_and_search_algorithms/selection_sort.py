# Selection sort
#
# Time: O(n^2)
from typing import List


def selection_sort(array: List) -> List:
    array_length = len(array)

    for i in range(0, array_length - 1):
        smallest = i

        for j in range(i + 1, array_length):
            if array[j] < array[smallest]:
                smallest = j

        array[i], array[smallest] = array[smallest], array[i]

    return array
