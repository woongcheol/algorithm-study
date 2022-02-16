N = int(input())
dot_list = list()
for _ in range(N):
    x, y = map(int, input().split())
    dot_list.append((x, y))

sorted_dot = sorted(dot_list, key=lambda x:(x[0], x[1]))

for x, y in sorted_dot:
    print(x, y)

    