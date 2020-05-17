N, M, X = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 10
ans = INF
# 2^N
for pat in range(1 << N):
	#print(pat)
	#print(format(pat, 'b').zfill(N))

	skill = [0 for _ in range(M)]
	cost = 0
	# pat 固定
	# N
	for bitno in range(N):
		# bitno = 0..N-1
		if pat & (1 << bitno) != 0:
			# M
			for i in range(M):
				skill[i] += C[bitno][i + 1]
			cost += C[bitno][0]
	#print(skill)
	#print(cost)
	if all([s >= X for s in skill]):
		ans = min(ans, cost)

if ans == INF:
	print(-1)
else:
	print(ans)


"""
O(2^N * N * M)
2^10 = 1024
2^30 ~= (10^3)^3 = 10^9
"""
"""
  11111101
&)00001000 (00000001 << 3 = 00001000)
----------
  00001000

x & 0 = 0
x & 1 = x
]]
"""
