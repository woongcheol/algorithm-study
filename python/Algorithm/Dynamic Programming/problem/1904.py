def total(N):
    number_list = [1, 1]
    if N == 1:
        print(number_list[N])
        return
    
    for i in range(2, N+1):
        number_list.append((number_list[i-1] + number_list[i-2]) % 15746)
    
    print(number_list[N])

N = int(input())
total(N)

