import sys
input = sys.stdin.readline

def f(n,m):
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1, m+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % (1000000007)
    return dp[n][m]
if __name__=='__main__':
    N, M = map(int, input().split())
    dp = [[0] * (M+1) for _ in range(N+1)]
    print(f(N,M))
    print(dp)