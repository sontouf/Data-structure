import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    stack = [(N-1,N-1)]
    result = 0
    while stack:
        cy, cx = stack.pop()
        if board[0][0] == -1:
            result = 1
            break
        for i in range(cy+1):
            for j in range(cx+1):
                if board[i][j]-(cy - i + cx - j) == 0:
                    board[i][j] = -1
                    stack.append((i,j))
    if result == 1:
        print("HaruHaru")
    else:
        print("Hing")