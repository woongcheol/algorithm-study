# 인접 리스트를 딕셔너리로 구현
# n 정점, m 간선
n, m = map(int, input().split())

a = dict()
for _ in range(m):
    e1, e2 = map(int, input().split())
    if e1 not in a:
        a[e1] = [e2]
    else:
        a[e1].append(e2)
    if e2 not in a:
        a[e2] = [e1]
    else:
        a[e2].append(e1)

print(a)

# 인접 리스트
# n 정점, m 간선
n, m = map(int, input().split())

# 초기화
a = [[] for _ in range(n)]

# 간선 연결
for _ in range(m):
    e1, e2 = map(int, input().split())
    a[e1].append(e2)
    a[e2].append(e1)

print(a)