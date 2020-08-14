import math

import helpers

def zeroDegree(polynomial):
    if 0 in polynomial:
        print('Unsolvable equation')
    else:
        print('All reals numbers are solutions')

def firstDegree(polynomial):
    result = 0

    if 0 in polynomial:
        number = polynomial[0] * -1
        result = number

    result *= (1 / polynomial[1])
    result = helpers.reduceNumber(result)

    print('The solution is:')
    print(result)
    return result


def secondDegree(polynomial):
    c = 0
    b = 0
    a = 0

    if 0 in polynomial:
        c = polynomial[0]
    if 1 in polynomial:
        b = polynomial[1]
    if 2 in polynomial:
        a = polynomial[2]

    discriminant = helpers.getDiscriminant(a, b, c)
    
    if discriminant > 0:

        squareRoot = helpers.getSquareRoot(discriminant)

        numerator1 = (b * -1) + squareRoot
        numerator2 = (b * -1) - squareRoot
        denominator = 2 * a

        result1 = helpers.reduceNumber(numerator1 / denominator)
        result2 = helpers.reduceNumber(numerator2 / denominator)

        print('Discriminant is strictly positive, the two solutions are:')
        print(result1)
        print(result2)
    elif discriminant == 0:
        result = helpers.reduceNumber((b * -1) / (2 * a))
        print('One result:', result)
    else:
        print('2 irrational solutions')
    

