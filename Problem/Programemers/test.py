# 첫번째 시도
def solution(prices):
    answer = []
    cnt = 0
    for i in range(len(prices)):
        # 마지막 요소 최종 입력
        if i == len(prices) - 1:
            answer.append(cnt)

        for j in range(i+1, len(prices)):
            
            # 주식가격이 상승 및 유지될 때 카운트
            if prices[i] <= prices[j]:
                cnt += 1
            
            # 하락 시 카운트 및 종료
            else:
                cnt += 1
                answer.append(cnt)
                cnt = 0
                break
            
            # 반복문 종료 시 카운트 추가
            if j == len(prices)-1:
                answer.append(cnt)
                cnt = 0                

    return answer

prices = [1, 2, 3, 1, 3, 0]
print(solution(prices))