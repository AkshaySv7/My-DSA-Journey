from collections import deque

def input_graph():
    print('Enter the adjacency matrix of the graph:')
    for i in range(n):
        graph[i] = list(map(int, input().split()))

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1

n = int(input('Enter the number of nodes: '))
graph = [[0] * n for _ in range(n)]
visited = [0] * n
input_graph()
start = int(input('Enter the starting node: '))
print(f'The path of BFS from node {start} is: ', end="")
bfs(start)
