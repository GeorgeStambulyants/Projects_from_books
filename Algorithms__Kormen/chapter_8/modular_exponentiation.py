# modular exponentiation
#


def modular_exponentiation(x: int, d: int, n: int) -> int:
    '''
        d - nonnegative, n - positive
        returns pow(x, d) % n
    '''
    if d == 0:
        return 1

    if d % 2 == 0:
        z = modular_exponentiation(x, d/2, n)
        return pow(z, 2) % n
    else:
        z = modular_exponentiation(x, (d-1)/2, n)
        return (pow(z, 2) * x) % n
