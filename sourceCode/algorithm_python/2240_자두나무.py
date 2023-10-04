import sys
input = sys.stdin.readline

def f(time, num, pos):
    if time == T:
        return 0
    if dp[time][num] != -1:
        return dp[time][num]
    
    if pos == arr[time]:
        collect = 1
    else:
        collect = 0
    
    result  = f(time+1,num,pos) + collect # 안바꿈
    if num >= 1:
        result = max(result, f(time+1,num-1,int(not pos)) + collect)
    dp[time][num] = result
    return result


if __name__=='__main__':
    T, W = map(int ,input().split())
    arr = []
    for _ in range(T):
        arr.append(int(input())-1)
    dp = [[-1] * (W+1) for _ in range(T)]
    print(f(0, W, 0))
    print(dp)