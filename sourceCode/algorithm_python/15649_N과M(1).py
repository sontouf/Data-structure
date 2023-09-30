import sys
input = sys.stdin.readline


# def dfs(path):
#     if len(path) == M:
#         print(*path)
#         return 
    
#     for i in range(1, N+1):
#         if i not in path:
#             dfs([*path, i])

# if __name__=='__main__':
#     N, M = map(int, input().split())

#     dfs([])

def dfs():
    if len(path) == M:
        print(*path)
        return 
    
    for i in range(1, N+1):
        if i not in path:
            path.append(i)
            dfs()
            path.pop()

if __name__=='__main__':
    N, M = map(int, input().split())
    path = []
    dfs()