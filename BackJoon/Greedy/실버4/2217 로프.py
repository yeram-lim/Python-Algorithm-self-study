N = int(input())
w_list = []
for i in range(N):
  w_list.append(int(input()))

w_list.sort(reverse=True)

use = [w_list[0]]
for i in range(1, N):
  curr = w_list[i - 1] * len(use)
  new = w_list[i] * (len(use) + 1)
  if curr < new:
    use.append(w_list[i])
  else:
    break
  
print(use[len(use) - 1] * len(use))