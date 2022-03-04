# 개인 풀이

def solved(N, S):
    result = 0
    bonus = 0
    for i in range(N):
        if S[i] == 'O':
            result += i+1
            result += bonus
            bonus += 1
        else:
            bonus = 0
    print(result)

N, S = int(input()), input()
solved(N, S)

# 강의 풀이
N, S = int(input()), input()
result, bonus = 0, 0
for idx, OX in enumerate(S):
    if OX == 'O':
        result, bonus = result+idx+1+bonus, bonus+1
    else:
        bonus = 0

    print(result)