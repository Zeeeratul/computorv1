import helpers

def zeroDegree(polynomial):
    if 0 in polynomial:
        print('No solution for this equation')
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
    denominator = 2 * a
    
    if discriminant > 0:
        squareRoot = helpers.getSquareRoot(discriminant)

        numerator1 = (b * -1) + squareRoot
        numerator2 = (b * -1) - squareRoot

        result1 = helpers.reduceNumber(numerator1 / denominator)
        result2 = helpers.reduceNumber(numerator2 / denominator)

        print('Discriminant is strictly positive, the two solutions are:')
        print(result1)
        print(result2)
    elif discriminant == 0:
        result = helpers.reduceNumber((b * -1) / (2 * a))
        print('Discriminant is equal zero, the only solution is:', result)
    else:
        discriminant *= -1
        squareRoot = helpers.getSquareRoot(discriminant)

        negativeBDivided = helpers.reduceNumber(b * -1 / denominator)
        squareRootDivided = helpers.reduceNumber(squareRoot / denominator)

        result1 = negativeBDivided + " + i * " + squareRootDivided
        result2 = negativeBDivided + " - i * " + squareRootDivided

        print('Discriminant is negative, the two complex numbers as solutions are:')
        print(result1)
        print(result2)