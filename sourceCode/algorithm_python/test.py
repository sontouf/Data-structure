from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6],
    4: [1],
    5: [2],
    6: [3]
}

def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end='->')
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)

    

    

if __name__=='__main__':
    visited = [0] * 7
    bfs(0)
