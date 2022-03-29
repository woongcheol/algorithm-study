# 개인 풀이
def b_sort(num, start, end):
    mid = (start+end)//2
    if num == num_lst[mid]:
        print(1)
        return
    if end < start:
        print(0)
        return
    if num > num_lst[mid]:
        b_sort(num, mid+1, end)
    elif num < num_lst[mid]:
        b_sort(num, start, mid-1)


N = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()
M = int(input())
check_lst = list(map(int, input().split()))

for num in check_lst:
    start = 0
    end = len(num_lst) - 1
    b_sort(num, start, end)

# 강의 풀이
N, num_lst = int(input()), {i: 1 for i in map(int, input().split())}
M = int(input())
for i in list(map(int, input().split())):
    print(num_lst.get(i, 0))