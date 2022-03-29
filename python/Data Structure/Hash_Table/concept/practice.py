# # hash table 생성
# '''
# 필요한 데이터 크기만큼 hash table을 생성해준다.
# '''
# from argon2 import hash_password


# hash_table = [i for i in range(10)]

# # hash function 구현
# '''
# 키 값을 받아 해싱 주소를 만든다.
# '''
# def hash_func(key):
#     return key % 5

# # hash table 저장
# '''
# 입력받은 data에서 키를 생성하고 이를 해싱 주소로 변환한다.
# '''
# def storage_data(data, value):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     hash_table[hash_address] = value

# # hash table 데이터 불러오기

# def get_data(data):
#     key = ord(data)
#     hash_address = hash_func(key)
#     hash_table[hash_address]

# storage_data('apple', 3000)
# storage_data('banana', 2000)
# storage_data('strawberry', 2000)

# get_data('apple')
# get_data('banana')
# get_data('strawberry')

# 리스트 변수를 활용해서 해쉬 테이블 구현
'''
hash 함수는 주피터를 킬 때마다 값이 달라지기 때문에 잘 사용하지 않는다.
'''
# print(hash("Dave"))

# 2. 자료구조와 해쉬 테이블
# hash_table = [0 for i in range(8)]

# def get_key(data):
#     return ord(data)

# def hash_function(key):
#     return key % 8

# def save_data(data, value):
#     hash_address = hash_function(get_key(data))
#     hash_table[hash_address] = value

# def read_data(data):
#     hash_address = hash_function(get_key(data))
#     return hash_table[hash_address]

# save_data('Dave', '0102030200')
# save_data('Andy', '01033232200')
# print(read_data('Dave'))

# print(hash_table)

# 충돌 해결 알고리즘 - changing 기법

# hash_table = [0 for i in range(3)]

# def get_key(data):
#     return hash(data)

# def hash_func(key):
#     return key % 3

# def save_data(data, value):
#     index_key = get_key(data)
#     hash_address = hash_func(index_key)
#     if hash_table[hash_address] != 0:
#         for idx in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][idx][0] == index_key:
#                hash_table[hash_address][idx][1] = value
#                return
#         hash_table[hash_address].append([index_key, value])
#     else:
#         hash_table[hash_address] = list([[index_key, value]])

# def read_data(data):
#     index_key = get_key(data)
#     hash_address = hash_func(index_key)
#     if hash_table[hash_address] != 0:
#         for idx in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][idx][0] == index_key:
#                 return hash_table[hash_address][idx][1]
#         return None
#     else:
#         return None

# save_data('Andy', '0123')
# save_data('Anna', '1234')
# save_data('Brown', '5678')
# save_data('Berlin', '8765')

# print(hash_table)

# print(read_data('Andy'))
# print(read_data('Anna'))
# print(read_data('Brown'))
# print(read_data('Berlin'))
# print(read_data('Max'))

# 충돌 해결 알고리즘 - Linear Probing 기법

# hash_table = [0 for i in range(5)]

# def get_key(data):
#     return hash(data)

# def hash_func(key):
#     return key % 5

# def save_data(data, value):
#     idx_key = get_key(data)
#     hash_address = hash_func(get_key(data))
#     if hash_table[hash_address] != 0:
#         for idx in range(hash_address, len(hash_table)):
#             if hash_table[idx] == 0:
#                 hash_table[idx] = [idx_key, value]
#                 return
#             elif hash_table[idx][0] == idx_key:
#                 hash_table[idx][1] == value
#                 return
#     else:
#         hash_table[hash_address] = [idx_key, value]

# def read_data(data):
#     idx_key = get_key(data)
#     hash_address = hash_func(get_key(data))
#     if hash_table[hash_address] != 0:
#         for idx in range(hash_address, len(hash_table)):
#             if hash_table[idx] == 0:
#                 return None
#             elif hash_table[idx][0] == idx_key:
#                 return hash_table[idx][1]
#         return None
#     else:
#         return None

# save_data('Andy', '0123')
# save_data('Anna', '1234')
# save_data('Brown', '5678')
# save_data('Berlin', '8765')

# print(hash_table)

# print(read_data('Andy'))
# print(read_data('Anna'))
# print(read_data('Brown'))
# print(read_data('Berlin'))
# print(read_data('Max'))

# 해시 함수 적용(SHA-1 / SHA-2)
import hashlib

hash_table = [0 for i in range(5)]

def get_key(data):
    hash_object = hashlib.sha1()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_func(key):
    return key % 5

def save_data(data, value):
    idx_key = get_key(data)
    hash_address = hash_func(get_key(data))
    if hash_table[hash_address] != 0:
        for idx in range(hash_address, len(hash_table)):
            if hash_table[idx] == 0:
                hash_table[idx] = [idx_key, value]
                return
            elif hash_table[idx][0] == idx_key:
                hash_table[idx][1] == value
                return
    else:
        hash_table[hash_address] = [idx_key, value]

def read_data(data):
    idx_key = get_key(data)
    hash_address = hash_func(get_key(data))
    if hash_table[hash_address] != 0:
        for idx in range(hash_address, len(hash_table)):
            if hash_table[idx] == 0:
                return None
            elif hash_table[idx][0] == idx_key:
                return hash_table[idx][1]
        return None
    else:
        return None

save_data('Andy', '0123')
save_data('Anna', '1234')
save_data('Brown', '5678')
save_data('Berlin', '8765')

print(hash_table)

print(read_data('Andy'))
print(read_data('Anna'))
print(read_data('Brown'))
print(read_data('Berlin'))
print(read_data('Max'))