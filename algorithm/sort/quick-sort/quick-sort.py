def quicksort(q):
    if len(q) <= 1:
        return q
    
    pivot = q[0]
    less = [x for x in q[1:] if x < pivot]
    greater = [x for x in q[1:] if x >= pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)

# 정렬하는 배열
myArray = [5, 2, 9, 3, 6, 1]

# 퀵 소트 함수 호출
sortedArray = quicksort(myArray)

# 정렬된 배열 출력
print(sortedArray)
