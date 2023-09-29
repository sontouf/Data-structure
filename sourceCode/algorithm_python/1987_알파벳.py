import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy ,sx):
    visited = []
    stack = []
    visited.append(graph[sy][sx])
    countMap[sy][sx] += 1
    stack.append((sy,sx))

    while stack:
        cy, cx = stack.pop()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=nx<C and 0<=ny<R:
                if graph[ny][nx] not in visited:
                    visited.append(graph[ny][nx])
                    stack.append((ny,nx))
                    countMap[ny][nx] = countMap[cy][cx] + 1
            print(countMap)
                
if __name__ == '__main__':
    global result
    R, C = map(int, input().split())
    graph = []
    countMap = [[0] * C for _ in range(R)]
    for i in range(R):
        graph.append(list(input().strip()))
    dfs(0,0)
    
    print(countMap)