# Quick sort
#
# Time: O(n*lg(n)) - this is not the worst.
# The worst time is O(n^2). This happens when the array is already sorted or
# it is sorted in descending order
#
# Sorting algorithm can be improved, if the pivot element is selected in
# a different way


def quick_sort(array, p, r):
    if p >= r:
        return

    q = partition(array, p, r)
    quick_sort(array, p, q - 1)
    quick_sort(array, q + 1, r)


def partition(array, p, r):
    q = p
    for u in range(p, r):
        if array[u] <= array[r]:
            array[q], array[u] = array[u], array[q]
            q += 1
    array[q], array[r] = array[r], array[q]

    return q
