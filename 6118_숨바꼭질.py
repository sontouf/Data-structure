import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        cur = queue.popleft()
        distance[cur] += 
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
    

if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    distance = [0] * (N+1)
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    

    bfs(1)
    print(distance)

    
