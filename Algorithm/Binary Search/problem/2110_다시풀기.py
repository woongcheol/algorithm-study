def wifi(house, spot):
    # 변수 선언 및 할당
    hlist = list()
    cnt = 0
    min = 0

    # 변수 데이터 입력
    for _ in range(house):
        hlist.append(int(input()))

    # 정렬
    hlist = sorted(hlist)

    if len(hlist) == 2:
        print(hlist[-1] - hlist[0])
    else:
        # 변수 선언
        start = 0
        end = len(hlist)-1

        # 이진 탐색 실행
        while cnt < spot - 2:
            # 최솟값 초기화
            min = 0

            # 이진 탐색 실행
            if cnt == 0:
                min, point, mid = binary_search(hlist, min, start, end)
            else:
                if point == start:
                    min, point, mid = binary_search(hlist, min, start, mid)
                else:
                    min, point, mid = binary_search(hlist, min, mid, end)
            

            # 반복 입력
            cnt += 1
        return print(min)


def binary_search(data, min, start, end):
    # 최소값일 경우 그대로 출력
    if min == 1:
        return 1
    
    # 조건 및 중앙값 선언
    mid = (end - start) // 2
    cond_1 = data[end] - data[mid]
    cond_2 = data[mid] - data[start]

    # 조건식 비교 - cond_2가 가장 가까운 경우
    if cond_1 > cond_2:
        if min < cond_2:
            return cond_2, start, mid
        else:
            min = cond_2
            mid = (mid + start)//2
            binary_search[data, min, start, mid]
    
    # 조건식 비교 - cond_1가 가장 가까운 경우
    else:
        if min < cond_1:
            return cond_1, end, mid
        else:
            min = cond_1
            mid = (mid + start)//2
            binary_search[data, min, mid+1, end]
        

N, C = map(int, input().split())
wifi(N, C)



