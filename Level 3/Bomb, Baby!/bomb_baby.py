def solution(m, f):
    int_m = int(m)
    int_f = int(f)
    mod_m = int_m % 2
    mod_f = int_f % 2
    impossible = 'impossible'

    if (int_m == int_f == 1):
        return '0'
    elif (mod_m == mod_f == 0) or (int_m == int_f):
        return impossible
    
    generations = 0

    while (int_m > 1 or int_f > 1):
        if (int_m > int_f):
            n_steps = num_steps(int_m, int_f)
            int_m -= n_steps * int_f
            generations += n_steps
        elif (int_f > int_m):
            n_steps = num_steps(int_f, int_m)
            int_f -= n_steps * int_m
            generations += n_steps
        else:
            break

    if (int_m != 1 or int_f != 1):
        return impossible

    return str(generations)

# calculates the number of times the smaller of the two arguments must be subtracted from the larger
# until the larger is equal or smaller than the initially smaller argument
def num_steps(larger, smaller):
    return -(-(larger - smaller) // smaller)