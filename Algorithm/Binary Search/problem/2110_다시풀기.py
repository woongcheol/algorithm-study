def wifi_max(N, C):
    # 좌표 리스트 생성
    house = list()
    for _ in range(N):
        house.append(int(input()))
    house = sorted(house)
    
    # Gap 갱신 - 변수 선언
    start = house[1] - house[0] # Gap 최솟값
    end = house[-1] - house[0] # Gap 최댓값
    result = 0

    # Gap 갱신 - 반복문
    while start <= end:
        mid = (start + end) // 2 # Gap 갱신
        value = house[0]
        count = 1

        # 첫 번째 인덱스에서 Gap을 적용한 인덱스 찾기
        for i in range(1, len(house)):
            if house[i] >= value + mid:
                value = house[i]
                count += 1
        
        # C개 이상 공유기를 설치할 수 있을 경우
        if count >= C:
            start = mid + 1
            result = mid
        
        # C개 이상 공유기를 설치할 수 없을 경우
        else:
            end = mid - 1
    
    print(result)

N, C = map(int, input().split())
wifi_max(N, C)