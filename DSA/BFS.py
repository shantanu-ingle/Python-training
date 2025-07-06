#Undirected : BFS

from collections import deque

adjacency_list = {
    '1':['4','2'],
    '2':['1','3'],
    '3':['2','4'],
    '4':['1','3'],
}

start = '4'

def bfs_undirected(adjacency_list,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs_undirected(adjacency_list,start)

