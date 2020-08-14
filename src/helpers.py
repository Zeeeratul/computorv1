def getSquareRoot(sqrtToFind, actualNb = 0, iterations = 1):

    if iterations == 100000000:
        return actualNb

    while actualNb ** 2 < sqrtToFind:
        actualNb = actualNb + (1 / iterations)

    if actualNb ** 2 != sqrtToFind:
        return getSquareRoot(sqrtToFind, actualNb - (1 / iterations), iterations * 10)
    else: 
        return actualNb

def getDegree(polynomial):
    polynomialDegree = 0
    for degree in polynomial:
        if degree > polynomialDegree:
            polynomialDegree = degree
    return polynomialDegree


def getDiscriminant(a, b, c):
    bSquare = b ** 2
    leftPart = -4 * a * c

    discriminant = bSquare + leftPart
    return discriminant