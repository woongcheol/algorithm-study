# 개인 풀이
N, M = map(int, input().split())
group = dict()
person = dict()

for _ in range(N):
    team = input()
    people = int(input())
    for _ in range(people):
        member = input()
        if team not in group:
            group[team] = list()
            group[team].append(member)
        else:
            group[team].append(member)
        person[member] = team

for _ in range(M):
    quiz = input()
    if int(input()) == 1:
        print(person[quiz])
    else:
        group[quiz].sort()
        for member in group[quiz]:
            print(member)

# 강의 풀이
N, M = map(int, input().split())
group, person = {}, {}

for _ in range(N):
    team, people = input(), int(input())
    group[team] = []
    for _ in range(people):
        member = input()
        group[team].append(member)
        person[member] = team

for _ in range(M):
    quiz, q = input(), int(input())
    if  q == 1:
        print(person[quiz])
    else:
        for member in sorted(group[quiz]):
            print(member)