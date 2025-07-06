# Directed : DFS

adjacency_list = {
    '1':['3'],
    '2':['1','4'],
    '3':['5'],
    '4':['5'],
    '5':[]
    }
start = '2'

def dfs_directed(adjacency_list, start):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
dfs_directed(adjacency_list, start)


