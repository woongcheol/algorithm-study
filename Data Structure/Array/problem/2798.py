def blackjack(N, M, card_number):
    max = 0
    for idx_1 in range(N-2):
        for idx_2 in range(idx_1 + 1, N-1):
            for idx_3 in range(idx_2 + 1, N):
                sum = card_number[idx_1] + card_number[idx_2] + card_number[idx_3]
                if sum == M:
                    return M
                elif sum < M and sum > max:
                    max = sum
    return max


N, M = map(int, input().split())
card_number = list(map(int, input().split()))
print(blackjack(N, M, card_number))

