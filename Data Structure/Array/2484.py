# 개인 풀이
def sum():
    result = 0
    if len(num_set) == 1:
        result = 50000 + cube_num[0] * 5000
    elif len(num_set) == 2:
        if cube_num.count(cube_num[0]) == 1 or cube_num.count(cube_num[0]) == 3:
            result = 10000 + cube_num[1] * 1000
        else:
            result = 2000 + cube_num[0] * 500 + cube_num[3] * 500
    elif len(num_set) == 3:
        for num in num_set:
            if cube_num.count(num) == 2:
                result = 1000 + num * 100
    else:
        result = cube_num[-1] * 100
    
    return result

N = int(input())
max = 0
for _ in range(N):
    cube_num = sorted(list(map(int, input().split())))
    num_set = set(cube_num)
    
    price = sum()

    if max < price:
        max = price

print(max)

# 강의 풀이
def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + (lst[1] + lst[2]) * 500
    for i in range(3):
        if lst[i] == lst[i+1]:
            return 1000 + lst[i] * 100
    return lst[-1] * 100

N = int(input())
print(max(money() for i in range(N)))