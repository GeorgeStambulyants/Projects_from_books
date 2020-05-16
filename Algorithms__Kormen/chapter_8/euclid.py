# Euclid's algoritm to find greatest common divisor (GCD)
#


def euclid(a: int, b: int) -> tuple:
    '''
        returns tuple (g, i, j) where g is GCD of a and b,
        and g == a*i + b*j
    '''
    if b == 0:
        return (a, 1, 0)

    (g, i_tmp, j_tmp) = euclid(b, a % b)

    i = j_tmp
    j = i_tmp - (a // b) * j_tmp

    return (g, i, j)
