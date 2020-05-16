N,A,B = map(int, input().split())

num_move = N // (A+B)
rest = N % (A+B)

if (rest > A):
    result = A*(num_move+1)
else:
    result = A*num_move+rest

print(result)
