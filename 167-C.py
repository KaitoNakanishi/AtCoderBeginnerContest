N, M, X = map(int,input().split())
C = [list(map(int, input().split())) for _ in range(N)]

result = 0
buy_or_not = [0 for i in range(N)]
skill = [0 for i in range(M)]

# buy all book
for i in range (N):
    result += C[i][0]
    buy_or_not[i] = 1

#print(buy_or_not)

for i in range (N):
    for j in range (M):
        skill[j] += C[i][j+1]
        print("skill[j]:", skill[j])
        print("C[i][j+1]:", C[i][j+1])

for i in range (N):
    flag = 1
    for j in range (M):
        if (skill[j] < C[i][j+1]):
            flag = 0
            print("flag=0")


N: 8 M: 5 X: 22
C: [
    [100, 3, 7, 5, 3, 1], 
    [164, 4, 5, 2, 7, 8], 
    [334, 7, 2, 7, 2, 9], 
    [234, 4, 7, 2, 8, 2], 
    [541, 5, 4, 3, 3, 6], 
    [235, 4, 8, 6, 9, 7], 
    [394, 3, 6, 1, 6, 2], 
    [872, 8, 4, 3, 7, 2]
]
result: 0
buy_or_not: [0, 0, 0, 0, 0, 0, 0, 0]
skill: [0, 0, 0, 0, 0]
