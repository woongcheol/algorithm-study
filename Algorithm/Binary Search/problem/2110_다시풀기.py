# 1차 시도
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

# 2차 시도
from sys import stdin
INPUT = stdin.readline

# 이분 탐색
def binary_search(position, start, end):
    if start > end:
        return
    
    global answer
    cnt = 1
    current = position[0]
    mid = (start + end) // 2

    for i in range(1, len(position)):
        if position[i] >= current + mid:
            current = position[i]
            cnt += 1

    if cnt >= C:
        answer = mid
        binary_search(position, mid+1, end)
    else:
        binary_search(position, start, mid-1)


# 데이터 입력
N, C = map(int, INPUT().split())
position = list()
for i in range(N):
    position.append(int(INPUT()))
position.sort()

# 최소거리 및 최대거리
start = 1
end = position[-1] - position[0]
answer = 0

binary_search(position, start, end)
print(answer)