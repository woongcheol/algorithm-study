# 개인 풀이
M_L, M_R, T_L, T_R = input().split()

M = [M_L, M_R]
T = [T_L, T_R]

set_M = set(M)
set_T = set(T)


M_win = 0
T_win = 0

for M_SRP in M:
    for T_SRP in T:
        if M_SRP == 'S' and T_SRP == 'R':
            T_win += 1
        elif M_SRP == 'R' and T_SRP == 'S':
            M_win += 1
        elif M_SRP == 'P' and T_SRP == 'S':
            T_win += 1
        elif M_SRP == 'S' and T_SRP == 'P':
            M_win += 1
        elif M_SRP == 'R' and T_SRP == 'P':
            T_win += 1
        elif M_SRP == 'P' and T_SRP == 'R':
            M_win += 1

if len(set_M) != len(set_T):
    if len(set_M) == 1 and M_win <= T_win:
        print('TK')
    elif len(set_T) == 1 and T_win <= M_win:
        print('MS')
    else:
        print('?')
    
else:
    if len(set_M) == 1:
        if M_win > T_win:
            print('MS')
        elif M_win < T_win:
            print('TS')
        else:
            print('?')
    else:
        print('?')
        
# 강의 풀이
ML, MR, TL, TR = ('SRP'.index(i) for i in input().split())

if ML == MR and (ML+1) % 3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL+1) % 3 in [ML, MR]:
    print('MS')
else:
    print('?')