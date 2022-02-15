def stack(nubmer):
    # 스택에 입력
    stack = []
    solution = []
    cnt = 0
    for num in range(1, len(number) + 1):
        stack.append(num)
        solution.append('+')

        # pop - 숫자와 스택이 같을경우
        while stack and stack[-1] == number[cnt]:
            stack.pop()
            solution.append('-')
            cnt += 1
    
    if stack == []:
        print('\n'.join(solution))
    else:
        print('NO')

number = []
data = int(input())
for _ in range(data):
    n = int(input())
    number.append(n)

stack(number)