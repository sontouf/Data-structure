import sys
from collections import deque

input = sys.stdin.readline

MAX = 100000

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        if cur == K:
            print(distance[cur])
            break
        for nx in (cur-1, cur+1, cur * 2):
            if 0<=nx<=MAX and not distance[nx]:
                distance[nx] = distance[cur] + 1
                queue.append(nx)
    

if __name__=='__main__':
    N, K = map(int, input().split())
    distance = [0] *(MAX+1)
    bfs(N)
