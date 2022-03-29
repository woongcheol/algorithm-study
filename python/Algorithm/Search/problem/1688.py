def look(data):
    left = list()
    right = list()
    
    # 왼쪽
    max = 0
    cnt = 0
    for idx in range(len(data)):
        if data[idx] > max:
            max = data[idx]
            cnt += 1
    print(cnt)

    
    
    # 오른쪽
    max = 0
    cnt = 0
    for idx in range(len(data)-1, -1, -1):
        if data[idx] > max:
            max = data[idx]
            cnt += 1
    print(cnt)

trophy_list = list()
N = int(input())
for _ in range(N):
    trophy_list.append(int(input()))
look(trophy_list)