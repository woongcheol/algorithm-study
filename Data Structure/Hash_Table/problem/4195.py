def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

# 테스트 케이스 입력
T = int(input())

# 반복 실행
for _ in range(T):
    
    # 친구 수 입력
    F = int(input())
        
    # 자료형 할당 및 초기화
    parent = dict()
    number = dict()

    for _ in range(F):
        
        # 친구 관계 입력
        x, y = input().split(' ')
        
        # 네트워크 생성
        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        # 네트워크 연결
        union(x, y)

        print(number[find(x)])