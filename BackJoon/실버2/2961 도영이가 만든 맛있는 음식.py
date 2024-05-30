import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
ingredients = []
for i in range(N):
    S, B = map(int, input().split())
    ingredients.append((S, B))

result = 1e9
for i in range(1, N + 1):
    combis = combinations(ingredients, i)

    for combi in list(combis):
        s = 1
        b = 0
        for ingredient in combi:
            s *= ingredient[0]
            b += ingredient[1]
        result = min(result, abs(s - b))
print(result)

# arr = ['A', 'B', 'C']
# nCr = itertools.combinations(ingredients, 2)
# print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 2
# 3 8
# 5 8
# 정답 : 1

# 4
# 1 7
# 2 6
# 3 8
# 4 9
# 정답 : 1