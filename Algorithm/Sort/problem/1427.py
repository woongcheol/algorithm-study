def merge(left, right):
    left_idx = 0
    right_idx = 0
    sorted = []

    while left_idx < len(left) and right_idx < len(right):
        # 같은 숫자가 있을 경우 계속해서 반복 -> <=로 표시
        if left[left_idx] <= right[right_idx]:
            sorted.append(right[right_idx])
            right_idx += 1
        elif left[left_idx] > right[right_idx]:
            sorted.append(left[left_idx])
            left_idx += 1
        
    if left_idx < len(left):
        sorted.extend(left[left_idx:])
    else:
        sorted.extend(right[right_idx:])
    
    return sorted

def merge_split(num):
    if len(num) <= 1:
        return num

    mid = len(num)//2

    left = merge_split(num[:mid])
    right = merge_split(num[mid:])

    return merge(left, right)

N = input()
num_list = list()
for item in N:
    num_list.append(int(item))

num_list = merge_split(num_list)
print(''.join(map(str, num_list)))