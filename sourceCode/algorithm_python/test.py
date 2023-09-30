import sys
input = sys.stdin.readline

def dfs(n)->int: # k번쨰에 n을 경로에 넣어보고 사이클에 속한 학생 수 출력
    nxt = graph[n]
    visited[n] = 1
    path.append(n)
    if visited[nxt] == 0:
        return dfs(nxt)
    else:
        if nxt in path:
            return path.index(n)-path.index(nxt)+1
        return 0
    


if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = [0] + list(map(int, input().split()))
        visited = [0] * (N+1)
        count = 0
        for i in range(1, N+1):
            if visited[i] == 0:
                path = []
                count += dfs(i)
        print(N - count)
