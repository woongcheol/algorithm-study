N = int(input())

person_list = list()

for idx in range(N):
    age, name = input().split()
    person_list.append((int(age), name, idx))

sorted_list = sorted(person_list, key=lambda x:(x[0], x[2]))

for age, name, idx in sorted_list:
    print(age, name)