# 개인 풀이
from collections import deque

N, M = map(int, input().split())
name_a, name_b = input().split()
name_a = deque(name_a)
name_b = deque(name_b)

text_cnt = {'A': 3, 'B': 2, 'C': 1,	'D': 2, 
            'E': 4,	'F': 3, 'G': 1, 'H': 3,
            'I': 1, 'J': 1, 'K': 3, 'L': 1,
            'M': 3, 'N': 2, 'O': 1, 'P': 2, 
            'Q': 2, 'R': 2, 'S': 1, 'T': 2, 
            'U': 1, 'V': 1, 'W': 1,	'X': 2,	 
            'Y': 2, 'Z': 1}

# 알파벳 조합
name_comb = [0] * (len(name_a) + len(name_b))
idx = 0

while name_a and name_b:
    name_comb[idx] = name_a.popleft()
    idx += 1
    name_comb[idx] = name_b.popleft()
    idx += 1

if not name_a:
    for i in range(len(name_comb)-idx):
        name_comb[idx+i] = name_b[i]
else:
    for i in range(len(name_comb)-idx):
        name_comb[idx+i] = name_a[i]

# 숫자 변환
for i in range(len(name_comb)):
    name_comb[i] = int(text_cnt[name_comb[i]])

# 숫자 더하기
while len(name_comb) != 2:
    for i in range(len(name_comb)-1):
        if name_comb[i] + name_comb[i+1] >= 10:
            name_comb[i] = name_comb[i] + name_comb[i+1] - 10
        else:
            name_comb[i] = name_comb[i] + name_comb[i+1]
    name_comb.pop()

# 숫자 출력
for idx, num in enumerate(name_comb):
    if idx == 0 and num == 0:
        continue
    print(num, end='')
print('%')

# 강의 풀이
N, M = map(int, input().split())
name_a, name_b = input().split()

# 알파벳 획수 리스트 생성 - ord 조합
alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# 문자 조합
name_comb = ''
min_len = min(N, M)
for i in range(min_len):
    name_comb += name_a[i] + name_b[i]

name_comb += name_a[min_len:] + name_b[min_len:]

# 숫자 변환
lst = [alp[ord(i)-ord('A')] for i in name_comb]

# 숫자 더하기
for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))