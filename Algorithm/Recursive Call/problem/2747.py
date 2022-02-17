def fibo_dp(num):
    num_list = [0 for _ in range(num+1)]
    num_list[1] = 1

    for idx in range(2, num+1):
        num_list[idx] = num_list[idx-1] + num_list[idx-2]
    return num_list[num]

N = int(input())
print(fibo_dp(N))