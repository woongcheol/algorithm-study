def bird(number):
    minute = 0
    num = 1
    while number != 0:
        if number - num >= 0:
            number -= num
            minute += 1
            num += 1
        else:
            num = 1
    print(minute)

number = int(input())
bird(number)
