def play_vol(N, S, M):
    V = list(map(int, input().split()))
    dp = [[False] * (M + 1) for _ in range(N+1)]
    dp[0][S] = True
    
    for i in range(N):
        for j in range(M+1):
            if not dp[i][j]:
                continue
            if j >= V[i]:
                dp[i+1][j - V[i]] = True
            if M >= j + V[i]:
                dp[i+1][j + V[i]] = True

    result = -1       
    for i in range(M, -1, -1):
        if dp[N][i]:
            result = i
            break
    
    print(result)

N, S, M = map(int, input().split())
play_vol(N, S, M)

