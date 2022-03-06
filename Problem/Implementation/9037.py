T = int(input())
for _ in range(T):
    kid_num, candy_num = int(input()), list(map(int, input().split()))

    # 캔디 보충
    for i in range(len(candy_num)):
        if candy_num[i] % 2 == 1:
            candy_num[i] += 1

    # 캔디 전달
    cnt = 0

    while len(set(candy_num)) != 1:
        cnt += 1
        add_candy = [0]*kid_num
        
        # 전달할 캔디 수
        for i in range(len(candy_num)):
            add_candy[i] = candy_num[i] // 2
        
        # 캔디 전달
        for i in range(1, len(candy_num)):
            candy_num[i] = candy_num[i] // 2
            candy_num[i] += add_candy[i-1]

            if i == len(candy_num) - 1:
                candy_num[0] = candy_num[0] // 2
                candy_num[0] += add_candy[-1]

        # 캔디 보충
        for i in range(len(candy_num)):
            if candy_num[i] % 2 == 1:
                candy_num[i] += 1

    print(cnt)