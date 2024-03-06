N = int(input())
minute_list = list(map(int, input().split()))
minute_list.sort()
total = 0
prev = 0
for min in minute_list:
    total += (prev + min)
    prev = prev + min
print(total)