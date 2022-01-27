# hash table 생성
'''
필요한 데이터 크기만큼 hash table을 생성해준다.
'''
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

storage_data('apple', 3000)
storage_data('banana', 2000)
storage_data('strawberry', 2000)

get_data('apple')
get_data('banana')
get_data('strawberry')