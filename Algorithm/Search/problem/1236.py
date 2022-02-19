def defense(data):
    # 변수 선언
    row = list()
    col = list()

    # 좌표 값 및 인원 리스트 생성
    for idx in range(len(data)):
        for idx2 in range(len(data[idx][1])):
            if data[idx][1][idx2] == 'X':
                row.append((idx, 1))
                col.append((idx2, 1))

    # 중복 값 제거
    srow = set(row)
    scol = set(col)

    # 행, 열 필요배치 인원 확인
    need_row = len(data) - len(srow)
    need_col = len(data[0][1]) - len(scol)

    # 필요배치 인원 최소화
    if need_row == need_col:
        print(need_row)
    elif need_row > need_col:
        print(need_row)
    elif need_row < need_col:
        print(need_col)
        
N, M = map(int, input().split())
point = list()

for idx in range(N):
    point.append((idx, input()))

defense(point)