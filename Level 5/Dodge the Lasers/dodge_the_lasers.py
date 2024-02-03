from decimal import Decimal, getcontext 

# set decimal precision to 200 places
getcontext().prec = 200

# square root of 2 to 100 decimal places
sqrt_2 = Decimal('1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727')

def solution(s):
    n = Decimal(s)

    return str(int(sum(n)))

# uses the recurrence formula I found on math.stackexchange (credited at the end of README) to calculate
# the sum of the sequence "A194102": S(n) = sum(floor(i * sqrt(2)), i = 1 -> n)
def sum(n):
    if n == 0:
        return 0

    n_prime = ((sqrt_2 - 1) * n) // 1

    return (n * n_prime) + (n * ((n + 1) / 2)) - (n_prime * ((n_prime + 1) / 2)) - sum(n_prime)