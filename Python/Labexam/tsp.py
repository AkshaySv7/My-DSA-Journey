import heapq
def tsp_gbfs(graph,start):
    n=len(graph)
    visited=[0]*n
    path=[]
    cost=0
    current=start
    visited[current]=True
    path.append(current)

    for _ in range (n-1):
        pq=[]
        for neighbor in range(n):
            if not visited[neighbor]:
                heapq.heappush(pq,(graph[current][neighbor],neighbor))
        if pq:
            next_cost,next_city=heapq.heappop(pq)
            cost+=next_cost
            visited[next_city]=True
            path.append(next_city)
            current=next_city
    cost+=graph[current][start]
    path.append(start)
    return path,cost    


def main():
    n=int(input("Enter number of cities:"))
    print("enter cost matrix")
    graph=[]
    for i in range(n):
        row=list(map(int,input(f"Row{i+1}:").split()))
        graph.append(row)

    start=int(input("enter the starting city"))
    path,cost= tsp_gbfs(graph,start)
    print(path)
    print(cost)
if __name__=="__main__":
    main()
    
