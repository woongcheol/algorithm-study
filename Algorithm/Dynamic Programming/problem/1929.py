# 1차 시도 - 시간 초과
# M, N = map(int, input().split())

# def check(number):
#     for i in range(2, number):
#         if number != i and number % i == 0:
#             return False
#     return True


# def prime_number(start, end):
#     for i in range(start, end+1):
#         if start == 1:
#             continue

#         if check(i):
#             print(i)

# prime_number(M, N)

# 2차 시도
M, N = map(int, input().split())
check_list = [0] * (N + 1)

def check(number, end):
    if check_list[number] == 1:
        return False
        
    for i in range(2, end):
        next = number * i
        if next > end:
            break
        elif not check_list[next]:
            check_list[next] = 1

    return True

def prime_number(start, end):
    if start > 2:
        for i in range(2, start):
            if check_list[i] == 1:
                continue
            for j in range(1, end):
                next = i * j
                if next > end:
                    break
                elif not check_list[next]:
                    check_list[next] = 1

    for i in range(start, end+1):
        if i == 1:
            continue

        if check(i, end):
            print(i)

prime_number(M, N)