def lcs(W1, W2):
    # dp 초기화
    dp = [[0] * (len(W2)+1) for _ in range(len(W1)+1)]

    # 점화식 수행
    for i in range(1, len(W1)+1):
        for j in range(1, len(W2)+1):
            if W1[i-1] == W2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    print(dp[len(W1)][len(W2)])

W1 = input()
W2 = input()
lcs(W1, W2)