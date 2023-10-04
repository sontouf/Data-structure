import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy,sx):
    path[board[sy][sx]] = 1
    max_distance = sum(path)
    if max_distance == 26:
        return 26
    for i in range(4):
        ny = dy[i] + sy
        nx = dx[i] + sx

        if 0<=ny<R and 0<=nx<C:
            if path[board[ny][nx]] == 0:
                max_distance = max(max_distance,dfs(ny,nx))
                path[board[ny][nx]] = 0
    return max_distance




if __name__=='__main__':
    R, C = map(int, input().split())
    board = [list(map(lambda x: ord(x)-ord('A'), input().strip())) for _ in range(R)]
    path = [0] * 26
    print(dfs(0,0))