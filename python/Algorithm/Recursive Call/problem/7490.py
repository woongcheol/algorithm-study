import copy

def reculsive(array, num):
    if len(array) == num:
        array_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    reculsive(array, num)
    array.pop()

    array.append('+')
    reculsive(array, num)
    array.pop()

    array.append('-')
    reculsive(array, num)
    array.pop()
    

T = int(input())

for _ in range(T):
    array = []
    array_list = []
    num = int(input())
    number_list = [n for n in range(1, num+1)]
    reculsive(array, num-1)

    for item in array_list:
        string = ""
        for idx in range(num-1):
            string += str(number_list[idx]) + item[idx]
        string += str(number_list[-1])
        if eval(string.replace(" ",'')) == 0:
            print(string)
    print()

    