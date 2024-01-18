# takes assigned graph node number and returns the original map coordinates for that node
def node_to_coord(x, w):
    return ((x // w, x % w))

# checks if coordinates are inside the bounds of the map
def in_bounds(i, j, h, w):
    if 0 <= i < h and 0 <= j < w:
        return True
    return False

# creates the graph starting from the station, allowing moves into walls but not out of walls
def construct_graph(map, h, w):
    graph = []

    num_nodes = h * w
    for current_node in range(num_nodes):
        i = node_to_coord(current_node, w)[0]
        j = node_to_coord(current_node, w)[1]
        graph.append([])

        if map[i][j] == 1:
            continue
        else:
            if in_bounds(i, j+1, h, w):
                graph[current_node].append(current_node + 1)
            if in_bounds(i+1, j, h, w):
                graph[current_node].append(current_node + w)
            if in_bounds(i, j-1, h, w):
                graph[current_node].append(current_node - 1)
            if in_bounds(i-1, j, h, w):
                graph[current_node].append(current_node - w)

    return graph

# reverses the map, so that the escape pod is at (0,0) and the station entrace at (h-1,w-1)
def reverse_map(map, h, w):
    reversed_map = []

    for i in range(h):
        reversed_map.append([])
        for j in range(w):
            reversed_map[i].append(map[-(i+1)][-(j+1)])

    return reversed_map

def solution(map):
    h = len(map)
    w = len(map[0])

    forward_graph = construct_graph(map, h, w)
    reversed_map = reverse_map(map, h, w)
    backwards_graph = construct_graph(reversed_map, h, w)

    distances_from_station = bfs(forward_graph)
    distances_from_escape_pod = bfs(backwards_graph)
    distances_from_escape_pod.reverse()
    
    return (final_distance_calculator(distances_from_station, distances_from_escape_pod))

# breadth first search to visit every node and find the distance from node 0
def bfs(graph):
    num_nodes = len(graph)
    visited = [0]
    queue = [0]
    distances = initialise_graph_distances(num_nodes)

    while queue:
        current_node = queue.pop(0)

        for next_node in graph[current_node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
                distances[next_node] = distances[current_node] + 1

    return distances


# initialise the distances list, assuming bfs will always start from node 0
def initialise_graph_distances(num_nodes):
    distances = []
    distances.append(1)
    for i in range (num_nodes - 1):
        distances.append(-1)
    return distances

# sums the distances for all mutually reachable nodes (from the station and the escape pods, 
# including walls), returning the shortest path length found
def final_distance_calculator(distances_forward, distances_backwards):
    return min([distances_forward[i] + distances_backwards[i] - 1 for i in range(len(distances_forward)) 
            if distances_forward[i] != -1 and distances_backwards[i] != -1])