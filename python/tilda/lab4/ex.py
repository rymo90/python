from queue import Queue
def bfs_connected_component(graph,start):
    notduble = []
    queue = Queue()
    queue.enqueue(start)
    while queue.isEmpty() == False:
        node = queue.dequeue()
        if node not in notduble:
            notduble.append(node)
            tarbort= graph[node]

            for elem in tarbort:
                queue.enqueue(elem)
    return notduble
# finding shortest path between 2 nodes fo a graph
def  bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    queue = Queue()
    queue.enqueue([start])
    if start == goal:
        return "that was easy ! start = goal"
        # keep looping for all posible path have been checked
    while queue.isEmpty()==False:
        path = queue.dequeue()
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.enqueue(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return "no but connected "
graph = {'A': ['B', 'C', 'E'],
         'B': ['D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B',],
         'E': ['B','A'],
         'F': ['C'],
         'G': ['C']
         }
print(bfs_connected_component(graph, 'A'))
print(bfs_shortest_path(graph, 'G','D'))
