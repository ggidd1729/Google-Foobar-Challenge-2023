def solution(s):
    n = int(s)
    sqrt_2 = 2 ** (1/2)

    return str(int(sum(n, sqrt_2)))

# finds integer floor of a float
def floor(float):
    return int(float // 1)

# uses the recurrence formula I found on math.stackexchange (credited at the end of README) to calculate
# the sum of the sequence "A194102": S(n) = sum(floor(i * sqrt(2)), i = 1 -> n)
def sum(n, sqrt_2):
    if n == 0:
        return 0

    n_prime = floor((sqrt_2 - 1) * n)

    return (n * n_prime) + (n * ((n + 1) / 2)) - (n_prime * ((n_prime + 1) / 2)) - sum(n_prime, sqrt_2)