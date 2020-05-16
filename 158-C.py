A, B = map(int, input().split())

price_list_A = []
price_list_B = []

for i in range(1, 100):
    price_list_A.append(int(i / 0.08))
    price_list_B.append(int(i / 0.10))

print(price_list_A[1])

for i in range(1, 100):
    if (price_list_A[i] <= i <= price_list_B[i+1]):
        print(i)
        break
    else:
        break


"""
while true:
    if (price_A - 1)*0.08 == A:
        price_A -= 1
    else:
        break

while true:
    if (price_B - 1)*0.10 == B:
        price_B -= 1
    else:
        break



price_list_A = []
price_list_B = []

for i in range(1, 100):
    price_list_A.append(i / 0.08)
    price_list_B.append(i / 0.10)

print(price_list_A[17],price_list_B[1])

if 
else:
    price = -1

print(prcie)
