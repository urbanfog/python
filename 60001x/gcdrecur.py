def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    return a if b == 0 else gcdRecur(b, a % b)

print(gcdRecur(1071,462))