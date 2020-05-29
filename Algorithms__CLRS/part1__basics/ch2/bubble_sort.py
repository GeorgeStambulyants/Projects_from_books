# Bubble sort
#
#Time: O(n^2)
#
#
def bubble_sort(A: list) -> None:
    arr_length = len(A)
    for i in range(arr_length - 1):
        for j in range(arr_length - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
