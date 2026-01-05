# 필요한 동전 개수의 최솟값
# 재귀를 해야하나...
# 조합을 써야하나
# 일단 큰 동전부터 채울수있도록 역순 정렬을 해두자
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

idx = 0
count = 0
while k > 0:
    if k - coins[idx] >= 0:
        k = k - coins[idx]
        count = count + 1
        # print(k)
    else:
        idx = (idx + 1) % len(coins)

print(count)
