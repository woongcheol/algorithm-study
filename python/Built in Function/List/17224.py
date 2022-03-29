# 개인 풀이
N, L, K = map(int, input().split())

problem = list()
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    problem.append((sub1, sub2))

problem.sort(key= lambda x:x[1])
print(problem)

result = 0
cnt = 0
for sub1, sub2 in problem:
    if cnt == K:
        break
    elif sub1 > L:
        continue
    elif sub2 <= L:
        result += 140
        cnt += 1
    elif sub2 > L:
        result += 100
        cnt += 1

print(result)

# 강의 풀이
N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# hard 문제
ans = min(hard, K) * 140

# easy 문제
if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)