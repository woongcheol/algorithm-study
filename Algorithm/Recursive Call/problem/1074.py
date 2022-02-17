def z_curve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y :
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return

    z_curve(n / 2, x, y)
    z_curve(n / 2, x, y + n / 2)
    z_curve(n / 2, x + n / 2, y)
    z_curve(n / 2, x + n / 2, y + n / 2)

N, X, Y = map(int, input().split())
result = 0
z_curve(2**N, 0, 0)

# 시간 초과
# 블로그 보며 다시 복기해보자
# https://ggasoon2.tistory.com/11