# 재귀 함수 - 보완
from collections import deque
import sys
sys.setrecursionlimit(100000000)

def find(n, k):
    if n == k:
        print(array[n])
        return
    
    for v in (n-1, n+1, 2*n):
        if 0 <= v < max and not array[v]:
            array[v] = array[n] + 1
            q.append(v)
    v = q.popleft()
    find(v, k)

n, k = map(int, input().split())
max = 100001
array = [0] * max
q = deque()
find(n, k)

# 반복문
from collections import deque
def find(n, k):
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < max and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

n, k = map(int, input().split())
max = 100001
array = [0] * max
q = deque([n])
print(find(n, k))

