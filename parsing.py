import sys
import re
import collections

def getPolynomial():
    if len(sys.argv) > 1:
        polynomialArray = sys.argv[1].split('=')

        leftSide = polynomialArray[0].strip()
        rightSide = polynomialArray[1].strip()

        monomialsLeftList = splitInMonomials(leftSide)
        monomialsRightList = splitInMonomials(rightSide)

        convertedMonomialsLeftList = convertMonomials(monomialsLeftList)
        convertedMonomialsRightList = convertMonomials(monomialsRightList)

        reducePolynomial = reducing(convertedMonomialsLeftList, convertedMonomialsRightList)
        sortedPolynomial = collections.OrderedDict(sorted(reducePolynomial.items()))

        return sortedPolynomial
    else:
        print('Please provided a correct argument')
        sys.exit()


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

def convertMonomials(monomialsList):
    monomialsDict = {}
    pattern = re.compile(r'(?P<sign>[+-])?(?P<coefficient>\d+[.]?\d*)\*X\^(?P<degree>\d+)')

    for monomial in monomialsList:
        sign = ""
        matches = pattern.match(monomial)

        coefficient = float(matches.group('coefficient'))
        degree = int(matches.group('degree'))

        if matches.group('sign'): sign = matches.group('sign')
        if sign == "-": coefficient *= -1

        if degree in monomialsDict:
            coefficient += monomialsDict[degree]
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

    return leftSide

def removeNullCoefficient(leftSide):
    degreeToDelete = []

    for degree in leftSide:
        if leftSide[degree] == 0:
            degreeToDelete.append(degree)

    for degree in degreeToDelete:
        del leftSide[degree]

    return leftSide