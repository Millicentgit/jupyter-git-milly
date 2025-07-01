MARGIN = 2

def divide(dividend, divisor):
    quotient = dividend / divisor
    return quotient

r1 = divide(10, 5)
r1 = r1 - MARGIN  # error source, should be an addition
r2 = divide(10, r1)  # raises a ZeroDivisionError