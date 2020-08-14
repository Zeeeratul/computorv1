import math

import helpers

def zeroDegree(polynomial):
    if 0 in polynomial:
        print('unsolvable')
    else:
        print('All reals numbers are solutions')

def firstDegree(polynomial):
    result = 0

    if 0 in polynomial:
        number = polynomial[0] * -1
        result = number

    result *= 1 / polynomial[1]

    print('The solution is:')
    print(result)
    return result


def secondDegree(polynomial):
    if 0 in polynomial:
        c = polynomial[0]
    if 1 in polynomial:
        b = polynomial[1]
    if 2 in polynomial:
        a = polynomial[2]

    discriminant = helpers.getDiscriminant(a, b, c)
    # print(discriminant)
    if discriminant > 0:

        # NEED TO DO A CUSTOM SQRT FUNCTION
        # squareRoot = math.sqrt(discriminant)
        squareRoot = helpers.getSquareRoot(discriminant)
        print(discriminant)
        print('sqrt:', squareRoot)
        # print(squareRoot)

        numerator1 = (b * -1) + squareRoot
        numerator2 = (b * -1) - squareRoot
        denominator = 2 * a

        result1 = numerator1 / denominator
        result2 = numerator2 / denominator
        print('2 solutions', result1, result2)
    elif discriminant == 0:
        result = (b * -1) / (2 * a)
        print('One result:', result)
    else:
        print('2 irrational solutions')
    

