def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9

def plus():
    return "+"
def minus():
    return "-"
def times():
    return "*"
def divided_by():
    return "//"

seven(times(five()))  # must return 35
four(plus(nine()))  # must return 13
eight(minus(three()))  # must return 5
six(divided_by(two()))  # must return 3