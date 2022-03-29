from collections import deque

# 함수 생성
def print_num(total, current, priority):

    # 초기화
    data = deque()
    check = True
    cnt = 0

    # 출력물 입력 - (순서, 우선순위)
    for idx, priority in enumerate(priority):
        data.append((idx, priority))
    
    # 출력
    while data:
        
        # 출력물 우선순위 판단
        for idx in range(1, len(data)):
            if data[0][1] < data[idx][1]:
                check = False
                break

        # 현재 출력할 문서의 우선순위가 가장 높을때
        if check:
            
            # 현재 출력할 문서가 궁금했던 문서일 경우
            if data[0][0] == current:
                cnt += 1
                return cnt
            
            else:
                data.popleft()
                cnt += 1
                check = True

        else:
            # 현재 출력할 문서의 우선순위가 낮을 경우
            data.append(data.popleft())
            check = True

# 입력 값
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    print(print_num(N, M, priority))