graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6],
    4: [1],
    5: [2],
    6: [3]
}

visited = [0] * 7
stack = []

def dfs(start: int)->None:
    stack.append(start)
    visited[start] = 1
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                stack.append(nxt)
                visited[nxt] = 1

dfs(0)



            
