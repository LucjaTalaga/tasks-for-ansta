from decimal import Decimal, getcontext

getcontext().prec = 3

def print_decimals(min, max):
    output = min
    while output <= Decimal(max):
        print(Decimal(output))
        output += 0.5

print_decimals(2, 5.5)