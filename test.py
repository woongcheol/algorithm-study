from collections import deque

def change(a):
    for i in range(1, len(a)):
        a[i] = i

    return a

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
cnt = 4
lst = deque([])

while cnt:
    cnt -= 1
    lst.append(change(b))
    print(lst)