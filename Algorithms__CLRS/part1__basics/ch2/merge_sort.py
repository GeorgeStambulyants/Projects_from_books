#
# Merge sort. Time: O(n*lg(n))
#
#
infinity = float('inf')


def merge(L: list, R: list) -> list:
    '''
        L, R - arrays to merge
        ----------------------
        Time: O(n)
    '''

    L.append(infinity)
    R.append(infinity)
    C = []

    i = j = 0
    for _ in range(len(L + R) - 2):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j += 1
    
    return C


def merge_sort(A: list) -> None:
    if len(A) <= 1:
        return None

    q = len(A) // 2
    L = A[:q]
    R = A[q:]
    merge_sort(L)
    merge_sort(R)
    
    C = merge(L, R)
    A[:] = C[:]
