import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


def dfs(sy ,sx):
    global answer

    if answer < len(path):
        answer = len(path)
    
    for i in range(4):
        ny = dy[i] + sy
        nx = dx[i] + sx
        if 0<=ny<R and 0<=nx<C:
            if visited[graph[ny][nx]] == 0:
                visited[graph[ny][nx]] = 1
                path.append(graph[ny][nx])
                dfs(ny, nx)
                visited[graph[ny][nx]] = 0
                path.pop()

if __name__ == '__main__':
    R, C = map(int, input().split())
    graph = [list(map(lambda x:ord(x)-ord('A'), input().strip())) for _ in range(R)]
    visited = [0] * 26
    path = [graph[0][0]]
    answer = 0
    visited[graph[0][0]] = 1
    dfs(0, 0)
    print(answer)
