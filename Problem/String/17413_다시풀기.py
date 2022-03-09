# 강의 풀이
S = input()
tmp, ans, ck = "", "", False

for chr in S:
    # 공백
    if chr == " ":
        if not ck:
            ans += tmp[::-1] + " "
            tmp = ""
        if ck:
            ans += " "
            
    # <
    elif chr == "<":
        ck = True
        ans += tmp[::-1] + "<"
        tmp = ""
    
    # >
    elif chr == ">":
        ck = False
        ans += ">"
        tmp = ""
    
    # 알파벳, 숫자
    else:
        if ck:
            ans += chr
        else:
            tmp += chr

if tmp:
    ans += tmp[::-1]
print(ans)