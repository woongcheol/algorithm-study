from sys import stdin
input = stdin.readline

def ck_text(text):
    stack = list()
    check_list = ["(", ")", "[", "]"]
    for chr in text:
        if chr in check_list:
            if chr == "(" or chr == "[":
                stack.append(chr)
            elif chr == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(chr)
                    break
            elif chr == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(chr)
                    break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")

text = list(input().rstrip())

while len(text) != 1:
    ck_text(text)
    text = list(input().rstrip())