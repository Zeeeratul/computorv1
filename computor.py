import parsing
import resolve
import helpers

def main():
    reducePolynomial = parsing.getPolynomial()
    helpers.printReduceForm(reducePolynomial)
    reducePolynomial = parsing.removeNullCoefficient(reducePolynomial)
    polynomialDegree = helpers.getDegree(reducePolynomial)

    print('Polynomial degree:', polynomialDegree)

    if polynomialDegree == 0:
        resolve.zeroDegree(reducePolynomial)
    elif polynomialDegree == 1:
        resolve.firstDegree(reducePolynomial)
    elif polynomialDegree == 2:
        resolve.secondDegree(reducePolynomial)
    else:
        print('The polynomial degree is stricly greater than 2, I can\'t solve.')

if __name__ == "__main__":
    main()