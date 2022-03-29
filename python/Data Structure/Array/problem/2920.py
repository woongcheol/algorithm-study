def music(data):
    if data == [1, 2, 3, 4, 5, 6, 7, 8]:
        return 'ascending'

    elif data == [8, 7, 6, 5, 4, 3, 2, 1]:
        return 'descending'

    else:
        return 'mixed'

N = list(map(int, input().split()))
print(music(N))