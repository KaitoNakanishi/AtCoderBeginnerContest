A,B,C,K = map(int, input().split())

S = A+B+C
result = 0

if ( K > (A+B) ):
    result = A*(1) + (K-(A+B))*(-1)
elif ( (A+B) >= K >= A):
    result = A*(1)
elif ( A > K ):
    result = K*(1)

print(result)
