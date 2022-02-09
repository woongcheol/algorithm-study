# 1. Bubble Sort
# import random

# def bubble_sort(data):
#     for idx in range(0, len(data)-1):
#         sorted = False
#         for idx2 in range(len(data)-idx-1):
#             if data[idx2] > data[idx2+1]:
#                 data[idx2], data[idx2+1] = data[idx2+1], data[idx2]
#                 sorted = True
#         if sorted == False:
#             break
#     return data

# data = random.sample(range(30), 10)
# print(data)
# print(bubble_sort(data))

# 2. Insert Sort
# import random

# def insert_sort(data):
#     for idx in range(1, len(data)):
#         for idx2 in range(idx, 0, -1):
#             if data[idx2] < data[idx2-1]:
#                 data[idx2], data[idx2-1] = data[idx2-1], data[idx2]
#             else:
#                 break
#     return data


# data = random.sample(range(30), 10)
# print(data)
# print(insert_sort(data))

# # 3. Select Sort
# import random

# def select_sort(data):
#     for i in range(len(data)):
#         for j in range(i+1, len(data)):
#             if data[i] > data[j]:
#                 data[i], data[j] = data[j], data[i]
#     return data

# data = random.sample(range(30), 10)
# print(data)
# print(select_sort(data))

# DP
# def squear(n):
#     for idx in range(2, n+1):
#         memory[idx] = memory[idx-1] + memory[idx-2]
#     return memory[n]

# n = int(input())
# memory = [0 for _ in range(0, n+1)]
# memory[0] = 1
# memory[1] = 1
# print(squear(n))

# # Quick Sort
import random
from collections import deque

def quick_sort(data):
    # 데이터가 1개일 경우 반환
    if len(data) <= 1:
        return list(data)

    # 변수 초기화
    pivot = data[0]
    left = deque()
    right = deque()

    # 피봇 기준 데이터 정렬
    for idx in range(1, len(data)):
        if pivot > data[idx]:
            left.appendleft(data[idx])
        else:
            right.append(data[idx])
    return quick_sort(left) + [pivot] + quick_sort(right)


data = deque(random.sample(range(30), 10))
print(quick_sort(data))

# Quick Sort - list comprehension
import random

def quick_sort(data):
    # 값이 1이 나오면 값 반환
    if len(data) <= 1:
        return data
    
    # 변수 초기화
    pivot = data[0]
    
    # 분류 - list comprehension
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    # recursive call
    return quick_sort(left) + [pivot] + quick_sort(right)

data = random.sample(range(30), 10)
print(quick_sort(data))