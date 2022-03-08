# 개인 풀이
def price(dict):
    if len(dict) == 1:
        for num in dict:
            total = 10000 + num * 1000
    elif len(dict) == 2:
        for num in dict:
            if dict[num] == 2:
                total = 1000 + num * 100
    elif len(dict) == 3:
        max = 0
        for num in dict:
            if max < num:
                max = num
        total = max * 100

    print(total)
    
cube_num = map(int, input().split())

num_dict = dict()

for data in cube_num:
    if data not in num_dict:
        num_dict[data] = 1
        continue
    num_dict[data] += 1

price(num_dict)

# 강의 풀이
def price():
    if len(cube_set) == 1:
        total = 10000 + cube_num[0] * 1000
    elif len(cube_set) == 2:
        total = 1000 + cube_num[1] * 100
    elif len(cube_set) == 3:
        total = cube_num[-1] * 100

    print(total)
    
cube_num = sorted(list(map(int, input().split())))
cube_set = set(cube_num)

price()