def check(num):
    for i in range(num):
        if row[num] == row[i]:
            return False
        if abs(row[num] - row[i]) == num - i:
            return False
    return True

def dfs(num):
    global result
    if num == n:
        result += 1
        return
    
    else:
        for i in range(n):
            row[num] = i
            if check(num):
                dfs(num+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)