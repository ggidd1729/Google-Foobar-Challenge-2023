def solution(entrances, exits, path):
    super_entrance = aggregate_entrances(entrances, path)
    super_exit = aggregate_exits(exits, path)

    # print("super entrance: ", super_entrance)
    # print("super exit: ", super_exit)

    return

# creates a virtual "super entrance" to simplify the multi-source, multi-sink max flow problem to single-
# -source, single-sink max flow
def aggregate_entrances(entrances, path):
    aggregated = path[entrances[0]]

    for entrance in range (1,len(entrances)):
        aggregated = [sum(i) for i in zip(aggregated, path[entrances[entrance]])]

    return aggregated

# creates a virtual "super exit" to simplify the multi-source, multi-sink max flow problem to single-
# -source, single-sink max flow
def aggregate_exits(exits, path):
    num_rooms = len(path[0])
    aggregated = [0] * num_rooms

    for room in path:
        for exit in exits:
            if room[exit] != 0:
                aggregated = [sum(i) for i in zip(aggregated, room)]
                break

    return aggregated


# solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) 
# solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])  