def solution(entrances, exits, path):
    super_entrance = aggregate_entrances(entrances, path)
    super_exit = aggregate_exits(exits, path)

    # print("super entrance: ", super_entrance)
    # print("super exit: ", super_exit)

    path.append(super_entrance)
    path.append(super_exit)

    return ford_fulkerson(path, -2, -1)

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

# breadth-first-search to find an augmenting from source to sink
def bfs(path, source, sink, parent):
    num_rooms = len(path)
    visited = [False] * num_rooms
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        current = queue.pop(0)
        for next in range(len(path[current])):
            if not visited[next] and path[current][next] > 0:
                queue.append(next)
                visited[next] = True
                parent[next] = current

    if visited[sink]:
        return True
    return False

#
def ford_fulkerson(path, entrance, exit):
    max_flow = 0

    return max_flow


# solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) 
# solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])  