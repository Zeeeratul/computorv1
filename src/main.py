import parsing
import resolve
import helpers

reducePolynomial = parsing.getPolynomial()
polynomialDegree = helpers.getDegree(reducePolynomial)
reduceForm = helpers.getReduceForm(reducePolynomial)

print('Reduced form:', reduceForm)
print('Polynomial degree:', polynomialDegree)

if polynomialDegree == 0:
    resolve.zeroDegree(reducePolynomial)
elif polynomialDegree == 1:
    resolve.firstDegree(reducePolynomial)
elif polynomialDegree == 2:
    resolve.secondDegree(reducePolynomial)
else:
    print('The polynomial degree is stricly greater than 2, I can\'t solve.')