# Selection Sort
#
# Time: O(n^2)
#
#
def selection_sort(A: list) -> None:
    for i in range(len(A) - 1):
        smallest_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[smallest_index]:
                smallest_index = j
        
        A[smallest_index], A[i] = A[i], A[smallest_index]
