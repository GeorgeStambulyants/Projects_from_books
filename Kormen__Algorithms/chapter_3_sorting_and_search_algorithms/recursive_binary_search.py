def recursive_binary_search(array, p, r, x):
    if p > r:
        return None

    q = (p + r) // 2
    if array[q] == x:
        return q
    elif array[q] > x:
        return recursive_binary_search(array, p, q-1, x)
    else:
        return recursive_binary_search(array, q+1, r, x)
