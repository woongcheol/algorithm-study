import queue

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_weight = 0
    cnt = 0
    exit = [[]]
    bridge_max = queue.Queue()
    
    # 트럭이 모두 건널 때까지 반복문 실행
    while truck_weights:
        for i in range(len(truck_weights)):
            # 소요 시간 관리
            cnt += 1
            

            # 트럭 이동 가능여부 확인, 상태 등록
            if sum_weight + truck_weights[i] <= weight and bridge_max.qsize() <= bridge_length:
                sum_weight += truck_weights[i]
                bridge_length -= 1
                bridge_max.put(truck_weights[i])

            for j in range(len(exit)):
                if exit[j]:
                    exit.append([cnt])

                exit[j].append(cnt)

            # 이동 시간 관리 - 트럭 도착시 이동 상태 삭제
            if len(exit[0]) > bridge_length:
                bridge_max.get()
                del truck_weights[0]

    answer = cnt[-1][-1]
    return answer

bridge_length = 2
weight = 10
truck_weights =	[7,4,5,6]
solution(bridge_length, weight, truck_weights)