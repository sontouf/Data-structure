def dfs(start, numbers, target):

	if not numbers:
		if start == target:
			return 1
		else:
			return 0
	cur = numbers.pop()
	res1 = dfs(start-cur, numbers, target)
	res2 = dfs(start+cur, numbers, target)
	numbers.append(cur)
	return res1 + res2

def solution(numbers, target):
	answer = dfs(0, numbers, target)

	return answer

if __name__=='__main__':
	print(solution([1,1,1,1,1], 3))
	print(solution([4,1,2,1], 4))
	
