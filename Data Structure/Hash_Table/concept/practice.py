# hash table 생성
'''
필요한 데이터 크기만큼 hash table을 생성해준다.
'''
from argon2 import hash_password


hash_table = [i for i in range(10)]

# hash function 구현
'''
키 값을 받아 해싱 주소를 만든다.
'''
def hash_func(key):
    return key % 5

# hash table 저장
'''
입력받은 data에서 키를 생성하고 이를 해싱 주소로 변환한다.
'''
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# hash table 데이터 불러오기

def get_data(data):
    key = ord(data)
    hash_address = hash_func(key)
    hash_table[hash_address]

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

hash_table = [0 for i in range(8)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))

print(hash_table)