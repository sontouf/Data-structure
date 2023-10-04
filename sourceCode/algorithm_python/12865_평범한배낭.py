def f(idx, total):
    # 가방에 물건 n 개를 넣거나 무게가 K이면
    if idx == N or total == K:
        return 0
    # 메모제이션 이미 값이 있으면 리턴
    if dp[idx][total] !=-1:
        return dp[idx][total]
    # 구현
    w, v = arr[idx]
    # idx 에 해당하는 물건 안 넣기.
    result = f(idx + 1, total)
    if total + w <= K: 
        result = max(result, f(idx + 1, total + w) + v)
    dp[idx][total] = result
    return result

if __name__=='__main__':
    N, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * K for _ in range(N)]
    print(f(0, 0))
    