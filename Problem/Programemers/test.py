from itertools import count


def solution(bridge_length, weight, truck_weights):
    answer = 0
    wg = 0
    cnt = 0
    on_bridge = []
    wg_bridge = []
    time = []
    bus = [number for number in range(len(truck_weights))]

    # 다리 진입 가능여부
    while True:
        cnt += 1
        # 다리 진입 가능여부 확인, 진입
        if truck_weights:
            if bridge_length >= len(on_bridge) + 1 and weight >= wg + truck_weights[0]:
                on_bridge.append(bus[0])
                wg += truck_weights[0]
                wg_bridge.append(truck_weights[0])
                del truck_weights[0]

        # 모두 이동 완료 시 종료
        elif truck_weights == 0:
            answer = cnt
            break
        
        # 시간 경과
        for i in range(len(on_bridge)):
            # if on_bridge[i] == bus[i]:
            time.append(bus[i])

        # 트럭 이동 완료
        if bus:
            if bridge_length == time.count(bus[0]):
                for _ in range(bridge_length):
                    time.remove(bus[0])
                del on_bridge[0]
                del bus[0]
                wg -= wg_bridge[0]
                del wg_bridge[0]

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)