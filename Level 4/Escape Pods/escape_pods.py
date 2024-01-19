def solution(entrances, exits, path):
    append_super_entrance(entrances, path)
    append_super_exit(exits, path)

    max_flow = ford_fulkerson(path, -2, -1)

    return max_flow

# creates a virtual "super entrance" to simplify the multi-entrance, multi-exit max flow problem to single-
# entrance, single-exit max flow, appends it to path and adjust the path nodes (rooms)
def append_super_entrance(entrances, path):
    num_rooms = len(path[0])
    super_entrance = [0] * num_rooms

    for entrance in range(len(entrances)):
        for next in path[entrance]:
            super_entrance[entrance] += next

    path.append(super_entrance)

    return

# creates a virtual "super exit" to simplify the multi-entrance, multi-exit max flow problem to single-
# entrance, single-exit max flow, appends it to path and adjust the path nodes (rooms)
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

# breadth-first-search to find an augmenting path from entrance to exit
def bfs(path, entrance, exit, parent):
    num_rooms = len(path)
    visited = [False] * num_rooms
    queue = []
    queue.append(entrance)
    visited[entrance] = True

    while queue:
        current = queue.pop(0)
        for next in range(len(path[current])):
            if not visited[next] and path[current][next] > 0:
                queue.append(next)
                visited[next] = True
                parent[next] = current
                
    if visited[exit]:
        return True
    return False

# Ford-Fulkerson algorithm for computing maximum flow in a flow network
def ford_fulkerson(path, entrance, exit):
    num_rooms = len(path)
    parent = [-1] * num_rooms
    max_flow = 0

    while bfs(path, entrance, exit, parent):
        min_flow = float("Inf")

        current_room = exit
        while current_room != entrance:
            min_flow = min(min_flow, path[parent[current_room]][current_room])
            current_room = parent[current_room]
 
        max_flow += min_flow

        current_room = exit
        while current_room != entrance:
            previous_room = parent[current_room]
            path[previous_room][current_room] -= min_flow
            path[current_room][previous_room] += min_flow
            current_room = parent[current_room]

    return max_flow