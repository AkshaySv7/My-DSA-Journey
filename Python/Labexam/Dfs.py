def input_graph():
    print('Enter the adjacency matrix of the graph:')
    for i in range(n):
        graph[i] = list(map(int, input().split()))

def dfs(start):
    print(start, end=" ")
    visited[start] = 1
    for i in range(n):
        if graph[start][i] == 1 and not visited[i]:
            dfs(i)

n = int(input('Enter the number of nodes: '))
graph = [[0]*n for _ in range(n)]
visited = [0]*n
input_graph()
start = int(input('Enter the starting node: '))
print(f'The path of DFS from node {start} is: ', end="")
dfs(start)
