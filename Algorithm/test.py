def reculsive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        reculsive(data-1)
        print(f'returned {data}')

reculsive(4)