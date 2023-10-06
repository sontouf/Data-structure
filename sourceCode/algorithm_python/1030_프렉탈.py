import sys
input = sys.stdin.readline

def fractal(l, point):
    y, x = point
    center = l // N
    if l == 1:
        return 0
    elif center * (N-K) // 2 <= x < center * (N+K) // 2 and center * (N-K) // 2 <= y < center * (N+K) // 2:
        return 1
    y %= center
    x %= center
    return fractal( center, (y,x))

if __name__=='__main__':
    S, N, K, y1, y2, x1, x2 = map(int, input().split())
    l = N ** S
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            print(fractal(l, (i,j)), end='')
        print()
