import sys
input = sys.stdin.readline

dy = [0,-1,0,1]
dx = [-1,0,1,0]


def dfs(sy ,sx):
    global answer
    visited[graph[sy][sx]] = 1
    if answer < sum(visited):
        answer = sum(visited)
    
    for i in range(4):
        ny = dy[i] + sy
        nx = dx[i] + sx
        if 0<=ny<R and 0<=nx<C:
            if visited[graph[ny][nx]] == 0:
                dfs(ny, nx)
                visited[graph[ny][nx]] = 0

if __name__ == '__main__':
    R, C = map(int, input().split())
    graph = [list(map(lambda x:ord(x)-ord('A'), input().strip())) for _ in range(R)]
    visited = [0] * 26
    answer = 0
    dfs(0, 0)
    print(answer)
