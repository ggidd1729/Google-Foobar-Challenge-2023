from itertools import combinations

def solution(num_buns, num_required):
    
    # no bunnies needed..?
    if num_required == 0:
        bun_list = []
        for bun in range(num_buns):
            bun_list.append([])
        return bun_list
    
    # give the same key to each bunny
    elif num_required == 1:
        bun_list = []
        for bun in range(num_buns):
            bun_list.append([0])
        return bun_list
    
    # we ran out of bunnies!
    elif num_required > num_buns:
        return None

    elif 1 < num_required <= num_buns:
        bun_list = []
        num_keys = choose(num_buns, num_required - 1)
        num_per_key = num_buns - num_required + 1
        total_num_keys = num_keys * num_per_key
        keys_per_bun = total_num_keys // num_buns

        """
        print(num_keys)
        print(num_per_key)
        print(total_num_keys)
        print(keys_per_bun)
        """

        combi = combinations(range(num_keys), keys_per_bun)
        for i in combi:
            bun_list.append(list(i))
        return bun_list
    
    # invalid input
    return None

# calculates the factorial of an integer
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return (n * factorial(n-1))

# calculates nCr
def choose(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))