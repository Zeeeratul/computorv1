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

def getReduceForm(reducePolynomials):
    reduceForm = ""

    for degree in reducePolynomials:
        numberReduced = reduceNumber(reducePolynomials[degree])
        
        if numberReduced[0] == "-":
            numberReduced = "- " + numberReduced[1:]
        else: 
            numberReduced = "+ " + numberReduced

        reduceForm +=  numberReduced + " * X^" + str(degree) + " "

    if reduceForm[0] == "+":
        reduceForm = reduceForm[2:]
    
    reduceForm = reduceForm + "= 0"
    return reduceForm

def reduceNumber(number):

    stringNumber = format(number, '.6f')
    index = len(stringNumber) - 1

    while stringNumber[index] == "0":
        index -= 1

    if stringNumber[index] == ".":
        index -= 1
    
    if (0 == float(stringNumber)):
        return "0"
    else:
        return stringNumber[: index + 1]