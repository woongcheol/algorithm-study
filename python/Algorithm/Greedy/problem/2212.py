import sys
INPUT = sys.stdin.readline

def solved(point, N):
    # 데이터 오름차순 정렬
    point.sort()

    # 집중국이 1개일 경우
    if len(point) == 1 or N == 1:
        total = point[-1] - point[0]
        print(total)
        return

    # 간격 리스트 생성
    dist = list()
    for idx in range(len(point)-1):
        dist.append(point[idx+1]-point[idx])

    # 거리 탐색
    cnt = 1
    while cnt != N:
        max = 0
        position = 0
        for idx, num in enumerate(dist):
            if max < num:
                max = num
                position = idx
        del dist[position]
        cnt += 1
    
    # 최소 길이 출력
    result = 0
    for data in dist:
        result += data

    print(result)

K = int(INPUT())
N = int(INPUT())
point = list(map(int, INPUT().split()))

solved(point, N)