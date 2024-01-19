def solution(entrances, exits, path):
    append_super_entrance(entrances, path)
    append_super_exit(exits, path)

    print(path)

    return ford_fulkerson(path, -2, -1, entrances)

# creates a virtual "super entrance" to simplify the multi-source, multi-sink max flow problem to single-
# source, single-sink max flow, appends it to path and adjust the path nodes (rooms)
def append_super_entrance(entrances, path):
    num_rooms = len(path[0])
    super_entrance = [0] * num_rooms

    for entrance in range(len(entrances)):
        for next in path[entrance]:
            super_entrance[entrance] += next

    path.append(super_entrance)

    return

# creates a virtual "super exit" to simplify the multi-source, multi-sink max flow problem to single-
# source, single-sink max flow, appends it to path and adjust the path nodes (rooms)
def append_super_exit(exits, path):
    num_rooms = len(path[0])
    super_exit = [0] * num_rooms
    path.append(super_exit)

    for room in path:
        room += 2 * [0]
        for exit in exits:
            if room[exit] != 0:
                room[-1] += room[exit]
                room[exit] = 0

    return

# breadth-first-search to find an augmenting from source to sink
def bfs(path, source, sink, parent, entrances):
    num_rooms = len(path)
    visited = [False] * num_rooms
    queue = []
    queue.append(source)
    initialise_visited(visited, source, entrances)

    while queue:
        current = queue.pop(0)
        for next in range(len(path[current])):
            if not visited[next] and path[current][next] > 0:
                queue.append(next)
                visited[next] = True
                parent[next] = current
    #print(visited)
    if visited[sink]:
        return True
    return False

#
def ford_fulkerson(path, entrance, exit, entrances):
    parent = [-1]* len(path)
    max_flow = 0

    bfs(path, entrance, exit, parent, entrances)

    #print(parent)

    return max_flow

#
def initialise_visited(visited, source, entrances):
    visited[source] = True
    for entrance in entrances:
        visited[entrance] = True



# solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) 
# solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])  