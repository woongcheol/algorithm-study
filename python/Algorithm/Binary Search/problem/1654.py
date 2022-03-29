K, N = map(int, input().split())
line_list = [int(input()) for _ in range(K)]
line_list.sort()
max_length = line_list[-1]
min_length = 1

def div_line(num, array, start, end):
    global min_length
    cnt = 0

    if start > end:
        print(min_length)
        return
    
    mid = (start + end) // 2

    for line in array:
        cnt += line // mid
    
    if cnt < num:
        div_line(num, array, start, mid-1)
    else:
        min_length = max(min_length, mid)
        div_line(num, array, mid+1, end)

div_line(N, line_list, min_length, max_length)