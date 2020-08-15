import random
import sys
import re

# for ((i=0; i<=100; i++)); do
#   python3 random_input.py | xargs python3 computor.py
# done

degree_zero = [ "%s * X^0",
            ]

degree_one = [  "%s * X^1",
    
            ]

degree_two = [  "%s * X^2",
   
            ]

MIN_RANGE = 0
MAX_RANGE = 100

def isInt(nb):
    try:
        int(nb)
    except ValueError:
        return 0
    return 1


def select_zero(empty_treshold, minus_treshold):
    rand = random.randint(0, 99)
    to_insert = ""
    if rand < empty_treshold:
        return ""
    elif rand < minus_treshold:
        to_insert += "-"
    random.shuffle(degree_zero)
    to_insert += degree_zero[0]
    if to_insert.find("%s") != -1:
        to_insert = to_insert % (random.randint(MIN_RANGE, MAX_RANGE))
    return to_insert + " "


def select_one(empty_treshold, minus_treshold):
    rand = random.randint(0, 99)
    to_insert = ""
    if rand < empty_treshold:
        return ""
    to_insert += "- " if random.randint(0, 99) < minus_treshold else "+ "
    random.shuffle(degree_one)
    to_insert += degree_one[0]
    if to_insert.find("%s") != -1:
        to_insert = to_insert % (random.randint(MIN_RANGE, MAX_RANGE))
    return to_insert + " "


def select_two(empty_treshold, minus_treshold):
    rand = random.randint(0, 99)
    to_insert = ""
    if rand < empty_treshold:
        return ""
    to_insert += "- " if random.randint(0, 99) < minus_treshold else "+ "
    random.shuffle(degree_two)
    to_insert += degree_two[0]
    if to_insert.find("%s") != -1:
        to_insert = to_insert % (random.randint(MIN_RANGE, MAX_RANGE))
    return to_insert + " "

def generate_terms():
    rand = random.randint(0, 99)
    if rand < 30:
        return "0"
    return select_zero(20, 40) + select_one(20, 40) + select_two(20, 40)

def main():

    lhs = select_zero(10, 30) + select_one(10, 25) + select_two(10, 25)
    rhs = generate_terms()
    lhs = re.sub(r"^\+ ", "", lhs)
    lhs = re.sub(r"^- ", "-", lhs)
    rhs = re.sub(r"^\+ ", "", rhs)
    rhs = re.sub(r"^- ", "-", rhs)

    if lhs == "0" or rhs == "":
        lhs = "0 * X^0"
    if rhs == "0" or rhs == "":
        rhs = "0 * X^0"
    expression = lhs + "= " + rhs
    print("\"" + expression.strip() + "\"")


if __name__ == "__main__":
    main()