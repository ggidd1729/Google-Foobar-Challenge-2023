def solution(x, y):
    set_x = set(x)
    set_y = set(y)

    if (len(x) > len(y)):
        set_difference = set_x - set_y
    else:
        set_difference = set_y - set_x

    return set_difference.pop()
