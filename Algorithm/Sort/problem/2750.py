# sort 알고리즘 - bubble, insert, merge, quick, selection

def bubble_sort(num):
    # 리스트 선언
    num_list = []
    sorted = False

    # 숫자 입력
    for _ in range(num):
        number = int(input())
        num_list.append(number)

    while not sorted:
        sorted = True
        for idx in range(len(num_list)-1):
            if num_list[idx] > num_list[idx+1]:
                num_list[idx], num_list[idx+1] = num_list[idx+1], num_list[idx]
                sorted = False
    
    # 출력
    for num in num_list:
        print(num)

def insert_sort(num):
    # 리스트 선언
    num_list = []
    sorted = False

    # 숫자 입력
    for _ in range(num):
        number = int(input())
        num_list.append(number)
    
    for idx in range(len(num_list)-1):
        for idx2 in range(idx + 1, 0, -1):
            if num_list[idx2 - 1] > num_list[idx2]:
                num_list[idx2 - 1], num_list[idx2] = num_list[idx2], num_list[idx2 - 1]
            else:
                break

    # 출력
    for num in num_list:
        print(num)    

def merge_sort(num):
    # 리스트 선언
    num_list = []

    # 숫자 입력
    for _ in range(num):
        number = int(input())
        num_list.append(number)

    # merge sort 알고리즘
    num_list = merge_split(num_list)

    # 출력
    for num in num_list:
        print(num)    


def merge(left, right):
    left_idx = 0
    right_idx = 0
    sorted = []

    # idx 초과 하지 않도록 실행
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            sorted.append(right[right_idx])
            right_idx += 1
        elif left[left_idx] < right[right_idx]:
            sorted.append(left[left_idx])
            left_idx += 1
    
    # idx가 left 또는 right를 모두 순회했을 경우
    if left_idx == len(left):
        sorted.extend(right[right_idx:])
    else:
        sorted.extend(left[left_idx:])
    
    return sorted

def merge_split(num):

    mid = len(num)//2

    if len(num) == 1:
        return num

    left = merge_split(num[:mid])
    right = merge_split(num[mid:])

    return merge(left, right)

# import sys

# sys.setrecursionlimit(99999)

def quick_sort(num):
    # 리스트 선언
    num_list = []

    # 숫자 입력
    for _ in range(num):
        number = int(input())
        num_list.append(number)

    num_list = quick(num_list)

    for num in num_list:
        print(num)

def quick(num):
    if len(num) <= 1:
        return num

    left = []
    right = []
    pivot = num[0]

    for idx in range(1, len(num)):
        if pivot > num[idx]:
            left.append(num[idx])
        else:
            right.append(num[idx])

    return quick(left) + [pivot] + quick(right)

def selection_sort(num):
    # 리스트 선언
    num_list = []

    # 숫자 입력
    for _ in range(num):
        number = int(input())
        num_list.append(number)

    # selection sort 알고리즘
    for idx in range(len(num_list)-1):

        # 최솟값 초기화
        min = num_list[idx]
        
        for idx2 in range(idx+1, len(num_list)):
            if min > num_list[idx2]:
                min = num_list[idx2]
                num_list[idx], num_list[idx2] = num_list[idx2], num_list[idx]         

    for num in num_list:
        print(num)


num = int(input())

selection_sort(num)