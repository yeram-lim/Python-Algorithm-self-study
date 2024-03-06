N = int(input())
minute_list = list(map(int, input().split()))
minute_list.sort()
answer = 0
for x in range(1, N+1):
    answer += sum(minute_list[0:x])  
print(answer)