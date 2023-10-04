import sys
input = sys.stdin.readline

def dfs(i):
    if len(path) == i:
        result = sum(path)
        if sum_path[result] == 0:
            sum_path[result] = 1
        return
    for num in nums:
        path.append(num)
        dfs(i)
        path.pop()

if __name__=='__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    K = int(input())

    path = []
    sum_path = [0] * (nums[N-1] * K + 1)
    for i in range(1, K+1):
        dfs(i)
    cur_num = 1

    for i in range(1,nums[N-1] * K):
        if sum_path[i] == 1:
            cur_num += 1
        else:
            break
    if cur_num % 2 == 0:
        print("holsoon win at", cur_num)
    else:
        print("jjaksoon win at", cur_num)