def book_name(book):
    book_list = dict()
    for idx in range(len(book)):
        if not book[idx] in book_list:
            book_list[book[idx]] = 1
        else:
            book_list[book[idx]] += 1
    sdict = sorted(book_list.items(), key = lambda x:x[0])
    sdict = sorted(sdict, key = lambda x:x[1], reverse=True)

    print(sdict[0][0])

book = list()
num = int(input())
for _ in range(num):
    book.append(input())

book_name(book)

