import sys

def merge(left, right):
    left_idx = 0
    right_idx = 0
    sorted = []
    while left_idx != len(left) and right_idx != len(right):
        if left[left_idx] > right[right_idx]:
            sorted.append(right[right_idx])
            right_idx += 1
        else:
            sorted.append(left[left_idx])
            left_idx += 1
    
    if right_idx == len(right) and left_idx < len(left):
        sorted.extend(left[left_idx:])
    elif left_idx == len(left) and right_idx < len(right):
        sorted.extend(right[right_idx:])

    return sorted

def merge_split(num_list):
    if len(num_list) == 1:
        return num_list

    mid = len(num_list)//2
    left = merge_split(num_list[:mid])
    right = merge_split(num_list[mid:])

    return merge(left, right)

N = int(input())
num_list = list()
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

sorted_list = merge_split(num_list)
for num in sorted_list:
    print(num)

