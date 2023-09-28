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

# dfs의 재귀 버전
def dfs(cur: int)-> None:
    visited[cur] = 1
    print(cur, end='->')
    for nxt in graph[cur]:
        if visited[nxt] == 0:
            dfs(nxt)

root = 0
dfs(root)

