import sys
import math
input = sys.stdin.readline

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(math.comb(M,N))