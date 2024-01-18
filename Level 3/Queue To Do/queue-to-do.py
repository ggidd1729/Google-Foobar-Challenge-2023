def solution(start, length):

    check_sum = 0

    for row in range(length):
        seq_start = start + (row * length)
        seq_end = seq_start + (length - 1) - row

        check_sum ^= xor_on_sequence(seq_start, seq_end)
    
    return check_sum

# calculates the XOR of a sequence of integers starting from `start` and ending at `end`
def xor_on_sequence(start, end):
    return (xor_to_n(start - 1) ^ xor_to_n(end))

# calculates XOR of a sequence from 0 to n
def xor_to_n(n):
    remainder = n % 4

    if (remainder == 0):
        return n
    elif (remainder == 1):
        return 1
    elif (remainder == 2):
        return n + 1
    else:
        return 0
    

# https://www.geeksforgeeks.org/find-xor-of-numbers-from-the-range-l-r/