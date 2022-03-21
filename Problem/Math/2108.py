N = int(input())
num_list = []

def min_max(list):
    ret = list[-1] - list[0]
    print(ret)

def mode(list):
    num_map = dict()
    max_num = 0
    mode_list = []
    ret_list = []

    for num in list:
        if not num in num_map:
            num_map[num] = 1
        else:
            num_map[num] += 1
        
        if num_map[num] >= max_num:
            max_num = num_map[num]
            mode_list.append((max_num, num))

    for mode, mode_num in mode_list:
        if mode == max_num:
            ret_list.append(mode_num)
    
    if len(ret_list) >= 2:
        print(ret_list[1])
    else:
        print(ret_list[0])

def median(list):
    mid = len(list) // 2
    print(list[mid])

def arithmetic_mean(list):
    ret = 0
    for num in list:
        ret += num
    ret = round(ret / len(list))
    print(ret)

def statistics(list):
    arithmetic_mean(list)
    median(list)
    mode(list)
    min_max(list)

for _ in range(N):
    num_list.append(int(input()))

num_slist = sorted(num_list)
statistics(num_slist)