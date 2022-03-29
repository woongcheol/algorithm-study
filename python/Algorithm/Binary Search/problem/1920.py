# 탐색 함수
def check(number, number_check):
    for num in number_check:
        print(binary(num, number, 0, len(number)-1))
 

# 이진 탐색 알고리즘
def binary(value, data, start, end):

    if start > end:
        return 0

    mid = (end + start) // 2

    if value == data[mid]:
        return 1

    elif value < data[mid]:
        return binary(value, data, start, mid - 1)

    elif value > data[mid]:
        return binary(value, data, mid + 1, end)

# 숫자 리스트 생성
N = int(input())
number = list(map(int, input().split()))
number.sort()

# 비교 리스트 생성
M = int(input())
number_check = list(map(int, input().split()))

# 이진 탐색
check(number, number_check)