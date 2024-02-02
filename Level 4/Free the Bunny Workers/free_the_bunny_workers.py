from itertools import combinations

def solution(num_buns, num_required):

    # invalid input
    if not (isinstance(num_buns, int) and isinstance(num_required, int)):
        return None
    
    # num_buns should we between 1 and 9
    if num_buns < 1 or num_buns > 9:
        return None
    
    # num_required can't be negative or more than num_buns
    if 0 <= num_required <= num_buns:
        bun_key_list = [[] for bun in range(num_buns)]
        num_keys_per_key = num_buns - (num_required - 1)

        current_key = 0
        for buns_for_current_key in combinations(range(num_buns), num_keys_per_key):
            for bun in buns_for_current_key:
                bun_key_list[bun].append(current_key)
            current_key += 1

        return bun_key_list
    
    # num_required out of range
    return None