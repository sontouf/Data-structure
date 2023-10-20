import sys
import copy
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(cur):
	if cur == T:
		print(visited)
		if result[0] == -1:
			result[0] = cost[0]
			result.append(copy.deepcopy(visited))
		elif result[0] > cost[0]:
			result[0] = cost[0]
			result.pop()
			result.append(copy.deepcopy(visited))
		return
	min = cost[1]
	max = cost[2]
	for nxt, c in graph[cur]:
		if nxt not in visited:
			total = 0
			if cost[3] == 0:
				total = 0
				cost[1], cost[2] = c, c
			else:
				if c < cost[1]:
					total = cost[1] - c
					cost[1] = c
				elif c > cost[2]:
					total = c - cost[2]
					cost[2] = c
				else:
					total = 0
			cost[0] += total
			print(cost)
			cost[3] += 1
			dfs(nxt)
			cost[3] -= 1
			cost[1] = min
			cost[2] = max
			cost[0] -= total
			visited.pop()

if __name__=='__main__':
	N, M, S, T = map(int ,input().split())
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		a, b, c = map(int, input().split())
		graph[a].append((b,c))
		graph[b].append((a,c))
	cost = [0,0,0,0]
	visited = [S]
	result = [-1,]
	dfs(S)
	print(result[0])
	print(*result[1])
		
