# 배열로 union-find 구현

# 부모 노드 찾기 - O(1)
def find(x):

    # 부모 노드와 자신의 값이 같다면 자신을 반환
    if x == parent[x]:
        return x

    # 부모 노드와 자신의 값이 다르다면,
    else:
        # 해당 부모 노드를 할당한다.
        p = find(parent[x])

        # 자신의 부모 노드를, 할당한 값으로 변환한다.
        parent[x] = p

        # 변환된 부모 노드를 반환한다.
        return parent[x]


# 부모노드 연결 - 일반적으로 O(N)
def union(x, y):
    # 부모 노드 찾기
    x = find(x)

    # 부모 노드 찾기
    y = find(y)

    # 부모 노드 연결하기
    parent[y] = x

parent = []

for i in range(0, 5):
    parent.append(i)

# parent = [0, 1, 2, 3, 4]

union(1, 4) # x = 1, y = 4, parent = [0, 1, 2, 3, 1]
union(2, 4) # x = 2, y = 4, parent = [0, 2, 2, 3, 1]

# 부모 노드 검색 및 같은 집합 찾기
for i in range(1, len(parent)):
    print(find(i), end=' ')

