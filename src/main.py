import parsing
import resolve
import helpers

result = parsing.getPolynomial()
leftSide = result[0]
rightSide = result[1]

monomialsLeftList = parsing.splitInMonomials(leftSide)
monomialsRightList = parsing.splitInMonomials(rightSide)

convertedMonomialsLeftList = parsing.convertMonomial(monomialsLeftList)
convertedMonomialsRightList = parsing.convertMonomial(monomialsRightList)

print(convertedMonomialsLeftList)
print(convertedMonomialsRightList)


# leftSide = {
#     0: -5.5,
#     1: -2,
# }

# rightSide = {
#     0: -6,
#     1: 3

# }

reducePolynomial = parsing.reducing(convertedMonomialsLeftList, convertedMonomialsRightList)

print(reducePolynomial)
# polynomialDegree = helpers.getDegree(reducePolynomial)

# print('Polynomial degree:', polynomialDegree)

# if polynomialDegree == 0:
#     resolve.zeroDegree(reducePolynomial)
# elif polynomialDegree == 1:
#     resolve.firstDegree(reducePolynomial)
# elif polynomialDegree == 2:
#     resolve.secondDegree(reducePolynomial)
# else:
#     print('The polynomial degree is stricly greater than 2, I can\'t solve.')