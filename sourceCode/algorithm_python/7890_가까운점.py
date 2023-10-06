import sys
from collections import defaultdict
input = sys.stdin.readline

def calcenterInCircumscriber(i,j,k):
    x1, y1 = nums[i]
    x2, y2 = nums[j]
    x3, y3 = nums[k]
    x1_2 = x1**2
    x2_2 = x2**2
    x3_2 = x3**2
    y1_2 = y1**2
    y2_2 = y2**2
    y3_2 = y3**2
    if x2-x1 == 0:
        y, x = 0.5*(y1+y2), 0.5*(1/(x3-x2))*(x3_2-x2_2+y3_2-y2_2-(y3-y2)*(y1+y2))
    elif x3-x2 == 0:
        y, x = 0.5*(y3+y2), 0.5*(1/(x2-x1))*(x2_2-x1_2+y2_2-y1_2-(y2-y1)*(y3+y2))
    elif y3-y1 == 0:
        y, x = 0.5*(1/(y2-y1))*(x2_2-x1_2+y2_2-y1_2-(x3+x1)*(x2-x1)), 0.5*(x3+x1)
    elif y2-y1 == 0:
        y, x = 0.5*(1/(y3-y2))*(x3_2-x2_2+y3_2-y2_2-(x2+x1)*(x3-x2)), 0.5*(x2+x1)
    else:
        y, x = 0.5*(2*x2+x1+x3+(y2_2-y1_2)/(x2-x1)+(y3_2-y2_2)/(x3-x2))*(1/(y3-y1)), 0.5*(1/(x2-x1))*((x2_2-x1_2+y2_2-y1_2)/(y2-y1))
    return (y,x)


def checkCircumscriber(i,j,k):
    targets = []
    center_y, center_x = calcenterInCircumscriber(i,j,k)
    for n in range(3, N+3):
        if ((center_x-nums[n][0])**2+(center_y-nums[n][1])**2 < (center_x-nums[i][0])**2+(center_y-nums[i][1])**2):
            if n != i and n != j and n != k:
                targets.append(n)
    return targets

def delaunayTriangulation(i,j,k):
    targets = checkCircumscriber(i,j,k)
    print(i,j,k, targets)
    if len(targets)==1 and targets[0] == k:
        targets.pop()
    if targets:
        for t in targets:
            delaunayTriangulation(i,j,t)
            delaunayTriangulation(i,k,t)
            delaunayTriangulation(j,k,t)
    else:
        if i>2 and j>2 and k>2:
            board[i].add(nums[j])
            board[i].add(nums[k])
            board[j].add(nums[i])
            board[j].add(nums[k])
            board[k].add(nums[i])
            board[k].add(nums[j])
        
    
            

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = [(-1,-1),(5,-1),(-1,5)]+[tuple(map(int, input().split())) for _ in range(N)]
        board = [set([]) for _ in range(N+3)]
        delaunayTriangulation(0,1,2)
        print(board)
        # for i in range(3,N+3):
        #     for b in board[i]:
                
        #     print(min(board[i]))