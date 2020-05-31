# Merge sort
#
# Time: O(n*lg(n)) - this is not the worst case.
# This algorithm sorts any array by this time



def merge_sort(array):
    if len(array) <= 1:
        return None
    p = 0
    r = len(array)
    q = (p + r) // 2
    left_arr = array[p:q]
    right_arr = array[q:r]
    merge_sort(left_arr)
    merge_sort(right_arr)

    merged_arr = merge(left_arr, right_arr)

    array[:] = merged_arr[:]


def merge(arr_1, arr_2):
    i = j = k = 0
    merged_arr = [0] * (len(arr_1) + len(arr_2))
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            merged_arr[k] = arr_1[i]
            i += 1
            k += 1
        else:
            merged_arr[k] = arr_2[j]
            j += 1
            k += 1

    while i < len(arr_1):
        merged_arr[k] = arr_1[i]
        i += 1
        k += 1

    while j < len(arr_2):
        merged_arr[k] = arr_2[j]
        k += 1
        j += 1

    return merged_arr
