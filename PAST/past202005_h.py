N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

cost = [] * L
cost[0] = 0


for i in range(L):
    # 行動1
    cost[i] = min(cost[i], cost[i - 1] + T1)

    # 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + T2 + T1)

    # 行動3
    if i >= 4:
        cost[i] = min(cost[i], cost[i] + T2 * 3 + T1)

    # ハードルがその場にあるか
    if i in x:
        cost[i] += T3

ans = cost[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, cost[i] + T1 // 2 + T2 * (2 * (L - i) - 1) // 2)

print(ans)
