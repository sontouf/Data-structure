import sys
input = sys.stdin.readline

def f(i): # i 점에 대한 국경까지의 거리 return
	if dp[i] != -1:
		return dp[i]
	target = []
	for j in range(M):
		if obstacle[i][1] > obstacle[j][1] and j != i:
			target.append(obstacle[j])			
		if obstacle[i][1] > obstacle[(j + M) % M][1] and j != i:
			target.append(obstacle[(j + M) % M])
		if not target:
			dp[i] = obstacle[i][1]
			dp[i + M] = f(i + M)
			break
		for t_x, t_y in target:
			if obstacle[i][0]

	return dp[i]

if __name__=='__main__':
	N, M = map(int, input().split())
	point = []
	obstacle = [0] * (M * 2)
	dp = [-1] * (M * 2)
	for _ in range(N):
		a = list(map(lambda x: ord(x) - ord('0'), input().strip()))
		point.append((a[1], a[3], a[6]))
	for i in range(M):
		a = list(map(lambda x: ord(x) - ord('0'), input().strip()))
		obstacle[i] = (a[1], a[3])
		obstacle[i + M] = (a[9], a[11])
	for i in range(M):
		f(i)



			

	