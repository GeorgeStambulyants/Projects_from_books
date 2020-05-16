#
# Time of compute_LCS_table: O(mn); m, n see in funcs docstring
#
# Time of assemble_LCS: O(m + n)
#


def compute_LCS_table(X, Y):
    '''
        X, Y - two strings with respective lengths m and n
        returns an array l == [[0..m], [0..n]], where
        the value of l[m][n] is the length of the longest
        common subsequence of X and Y
    '''
    m = len(X)
    n = len(Y)
    l = [[j for j in range(n + 1)] for i in range(m + 1)]
    print(l)
    for i in range(m + 1):
        l[i][0] = 0
    for j in range(n + 1):
        l[0][j] = 0


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i][j - 1], l[i - 1][j])
    return l


def assemble_LCS(X, Y, l, i, j):
    '''
        X, Y, m, n - the same as in compute_LCS_table
        l - returned array from compute_LCS_table
        returns the longest common subsequence in X[i] and X[j]
    '''
    if l[i][j] == 0:
        return ''

    if X[i - 1] == Y[j - 1]:
        return assemble_LCS(X, Y, l, i-1, j-1) + X[i - 1]  # or Y[j]

    if l[i][j - 1] > l[i - 1][j]:
        return assemble_LCS(X, Y, l, i, j-1)

    if l[i][j - 1] <= l[i - 1][j]:
        return assemble_LCS(X, Y, l, i-1, j)


if __name__ == '__main__':
    print('TESTS:\n')
    X = 'CATCGA'
    Y = 'GTACCGTCA'
    l = compute_LCS_table(X, Y)

    print('Testing compute_LCS_table...\n')
    print('testcase#1:')
    if l[5][8] == 3:
        print('OK')
    else:
        raise AssertionError(f'{l[5][8]} != 3')

    print('testcase#2')
    if l[6][9] == 4:
        print('OK')
    else:
        raise AssertionError(f'{l[6][9]} != 4')

    print('testcase#3')
    if l[0][9] == 0:
        print('OK')
    else:
        raise AssertionError(f'{l[6][9]} != 0')

    print('testcase#4')
    if l[4][0] == 0:
        print('OK')
    else:
        raise AssertionError(f'{l[0][0]} != 0')

    print('testcase#5')
    if l[0][0] == 0:
        print('OK')
    else:
        raise AssertionError(f'{l[0][0]} != 0')

    print('testcase#6')
    if l[4][5] == 2:
        print('OK')
    else:
        raise AssertionError(f'{l[4][5]} != 2')

    print('------------------------')
    print('Testing assemble_LCS')

    print('\ntestcase#1')
    if assemble_LCS(X, Y, l, 5, 8) in ['ACG', 'ATC', 'CTC']:
        print('OK')
    else:
        raise AssertionError(f'{assemble_LCS(X, Y, l, 5, 8)} not in ["ACG", "ATC", "CTC"]')

    print('testcase#2')
    if assemble_LCS(X, Y, l, 6, 9) in ['CATC', 'CTCA']:
        print('OK')
    else:
        raise AssertionError(f'{assemble_LCS(X, Y, l, 6, 9)} not in ["CATC", "CTCA"]')

    print('testcase#3')
    if assemble_LCS(X, Y, l, 6, 0) == '':
        print('OK')
    else:
        raise AssertionError(f'{assemble_LCS(X, Y, l, 6, 0)} != ""')

    print('testcase#4')
    if assemble_LCS(X, Y, l, 0, 5) == '':
        print('OK')
    else:
        raise AssertionError(f'{assemble_LCS(X, Y, l, 0, 5)} != ""')

    print('testcase#5')
    if assemble_LCS(X, Y, l, 0, 0) == '':
        print('OK')
    else:
        raise AssertionError(f'{assemble_LCS(X, Y, l, 0, 0)} != ""')
