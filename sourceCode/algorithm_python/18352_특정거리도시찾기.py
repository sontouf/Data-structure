import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
	queue = deque()
	queue.append(v)
	visited = [0] * (N + 1)
	distance = [0] * (N + 1)
	visited[v] = 1
	while queue:
		cur = queue.popleft()
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				distance[nxt] = distance[cur] + 1
				queue.append(nxt)
				if distance[nxt] == K:
					result.append(i)

if __name__=='__main__':
	N, M, K, X = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
	result = []
	bfs(X)
	if result:
		result.sort()
		for i in result:
			print(i)
	else:
		print(-1)
