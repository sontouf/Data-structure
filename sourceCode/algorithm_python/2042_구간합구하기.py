import sys
input = sys.stdin.readline

if __name__=='__main__':
    N, M, K = map(int, input().split())
    nums = [0] + [int(input()) for _ in range(N)]
    for _ in range(M+K):
        a, b, c = map(int,input().split())
        if a == 1:
            nums[b] = c
        elif a == 2:
            print(sum(nums[b:c+1]))