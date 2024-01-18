# sum all the numbers in a list together
def prod(xs):
    result = 1

    for x in xs:
        result *= x
    
    return result


def solution(xs):
    
    if len(xs) == 1:
        return str(xs[0])
        
    xs.sort()
    
    negatives = []
    positives = []
    
    for x in xs:
        if x == 0:
            continue
        elif x < 0:
            negatives.append(x)
        else:
            positives.append(x)

    max_power = 0
    
    if len(positives) == 0:
        pass
    else:
        max_power += prod(positives)
    
    if len(negatives) < 2:
        pass
    elif len(negatives) % 2 == 0:
        max_power = max(max_power + prod(negatives), max_power * prod(negatives))
    else:
        negatives.pop()
        max_power = max(max_power + prod(negatives), max_power * prod(negatives))

    return str(max_power)