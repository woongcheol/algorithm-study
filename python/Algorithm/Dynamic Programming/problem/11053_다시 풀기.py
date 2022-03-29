from re import L


def lis(N):
    array = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

N = int(input())
lis(N)