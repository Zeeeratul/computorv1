import sys
import re

def getPolynomial():
    if len(sys.argv) > 1:
        return parsePolynomial(sys.argv[1])
    else:
        print('no argument exit program')
        sys.exit()

def parsePolynomial(string):
    polynomialArray = string.split('=')

    leftSide = polynomialArray[0].strip()
    rightSide = polynomialArray[1].strip()

    return [leftSide, rightSide]

def splitInMonomials(polynomial):

    monomialsList = []
    startIndex = 0
    index = 0

    while index < len(polynomial):

        if (polynomial[index] == "-" or polynomial[index] == "+") and index != startIndex:
            monomialsList.append(polynomial[startIndex : index].replace(" ", ""))
            startIndex = index
        index += 1

    monomialsList.append(polynomial[startIndex : index].replace(" ", ""))

    return monomialsList

def convertMonomial(monomialsList):

    monomialsDict = {}
    pattern = re.compile(r'(?P<sign>[+-])?(?P<coefficient>\d+[.]?\d*)\*X\^(?P<degree>\d+)')

    for monomial in monomialsList:
        sign = ""
        matches = pattern.match(monomial)

        coefficient = float(matches.group('coefficient'))
        degree = int(matches.group('degree'))

        if matches.group('sign'): sign = matches.group('sign')
        if sign == "-": coefficient *= -1

        monomialsDict.update({ degree: coefficient })

    return monomialsDict

def reducing(leftSide, rightSide):
    for degree in rightSide:
        number = rightSide[degree] * -1

        if degree in leftSide:
            result = leftSide[degree] + number
            if result == 0:
                del leftSide[degree]
            else:
                leftSide.update({ degree: result })
        else:
            if number != 0:
                leftSide.update({ degree: number })

    # REMOVE ALL 0 COEFFICIENT

    degreeToDelete = []

    for degree in leftSide:
        if leftSide[degree] == 0:
            degreeToDelete.append(degree)

    for degree in degreeToDelete:
        del leftSide[degree]

    return leftSide