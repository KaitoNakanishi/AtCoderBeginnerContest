N, M, X = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 10
ans = INF

def func(state):
	skill = [0 for _ in range(M)]
	cost = 0
	for bitno in range(N):
		# bitno = 0..N-1
		if state[bitno]:
			# M
			for i in range(M):
				skill[i] += C[bitno][i + 1]
			cost += C[bitno][0]
	if all([s >= X for s in skill]):
		global ans
		ans = min(ans, cost)

# try all pattern: i..N-1 bit
def rec(state, i):
	if i >= len(state):
		func(state)
		return

	state[i] = False
	# i+1 .. N-1
	rec(state, i + 1)

	state[i] = True
	rec(state, i + 1)

state = [False] * N
# ''0''..N-1
rec(state, 0)

if ans == INF:
	print(-1)
else:
	print(ans)
