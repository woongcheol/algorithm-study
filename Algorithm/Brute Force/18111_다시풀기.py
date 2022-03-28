from cmath import inf
from sys import stdin
input = stdin.readline



def block(lst, start, end):
    global max_height
    global height
    origin_b = B
    cnt = end + 1
    min_time = inf
    max_height = 0

    while cnt != start-1:
        b = origin_b
        cnt -= 1
        ck_time = 0
        need_b = cnt * N * M
        
        if now_block + origin_b < need_b:
            continue
        else:
            for i in range(N):
                for j in range(M):
                    if lst[i][j] == cnt:
                        continue
                    elif lst[i][j] > cnt:
                        b += 1 * (lst[i][j]-cnt)
                        ck_time += 2 * (lst[i][j]-cnt)
                    elif lst[i][j] < cnt:
                        b -= 1 * (cnt-lst[i][j])
                        ck_time += 1 * (cnt-lst[i][j])
        if min_time > ck_time:
            min_time = ck_time
            max_height = cnt
        else:
            print(min_time, max_height)
            break

N, M, B = map(int, input().split())
point = list()
min_b = 256
max_b = 0
now_block = 0
height = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    
    # 현재 모든 블럭 수
    now_block += sum(temp)

    # 최대, 최소 높이 확인
    max_height = max(temp)
    min_height = min(temp)
    max_b = max(max_b, max_height)
    min_b = min(min_b, min_height)

    # 블록 리스트 생성
    point.append(temp)


block(point, min_b, max_b)