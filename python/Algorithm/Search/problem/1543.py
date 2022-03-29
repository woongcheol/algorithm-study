def search(text, word):
    key = 0
    cnt = 0
    length = len(word)
    while key + length - 1 < len(text):
        if text[key:key+length] == word:
            cnt += 1
            key += len(word)
        else:
            key += 1
    
    print(cnt)

text = input()
word = input()
search(text, word)