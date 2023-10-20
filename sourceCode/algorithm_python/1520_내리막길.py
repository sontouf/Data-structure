import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy,sx):
    if sy == M-1 and sx == N-1:
        return 1
    if dp[sy][sx] != -1:
        return dp[sy][sx]
    way = 0
    for i in range(4):
        ny, nx = dy[i] + sy, dx[i] + sx
        if 0<=ny<M and 0<=nx<N and board[ny][nx] < board[sy][sx]:
                way += dfs(ny, nx) 
    dp[sy][sx] = way
    return dp[sy][sx]


if __name__=='__main__':
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]
    print(dfs(0,0))
    print(dp)