import sys
input = sys.stdin.readline

def dfs(cur:int)->int:
    stack.append(cur)
    visited[cur] = 1
    result = 0
    while stack:
        cur = stack.pop()
        nxt = graph[cur]
        cycle.append(cur)
        if visited[nxt] == 1:
            if nxt in cycle:
                break  
            return 0
        else:
            stack.append(nxt)
            visited[nxt] = 1
            cur = nxt
    result = cycle.index(cur) - cycle.index(nxt) + 1
    return result


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        count = 0
        graph = [0] + list(map(int, input().split()))
        visited = [0] * (N + 1)
        for i in range(1,N+1):
            if visited[i] == 0:
                cycle = []
                stack = []
                count += dfs(i)
        print(N-count)
