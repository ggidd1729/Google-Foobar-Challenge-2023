def solution(l, t):

    for i in range(len(l)):
        x = l[i]
        if x == t:
            return [i, i]

        sum = x
        j = i + 1
        while sum < t  and j < len(l):
            sum += l[j]
            if sum == t:
                return [i, j]
            j+=1

    return [-1, -1]