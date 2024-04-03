N = int(input())
result = 0
plus = []
minus = []
zero = []
for i in range(N):
    num = int(input())
    if num < 0:
        minus.append(num)
    elif num == 0:
        zero.append(num)
    elif num == 1:
        result += num
    else:
        plus.append(num)

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        result += (plus[i] * plus[i + 1])
    else:
        result += plus[i]

for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        result += (minus[i] * minus[i + 1])
    else:
        if len(zero) < 1:
            result += minus[i]

print(result)

# 4
# -1
# 2
# 1
# 3

# 5
# -27
# -30
# -5
# 2
# 5