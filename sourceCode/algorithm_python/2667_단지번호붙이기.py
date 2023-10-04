import sys
input = sys.stdin.readline
from collections import deque


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx)->int:
    graph[sy][sx] = 0
    queue = deque()
    queue.append((sy,sx))
    count = 1
    while queue:
        cy ,cx = queue.popleft()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny,nx))
                    count += 1
    return count




if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    component = []
    component = [bfs(y,x) for x in range(M) for y in range(N) if graph[y][x] == 1]
    component.sort()
    print(len(component))
    print(*component, sep='\n')
