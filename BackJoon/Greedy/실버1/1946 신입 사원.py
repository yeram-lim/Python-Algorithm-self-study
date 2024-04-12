T = int(input())
picked = []
for i in range(T):
  N = int(input())
  grades = []
  for j in range(N):
    grades.append(list(map(int, input().split())))
    
  grades.sort(key=lambda x : x[0]) #[[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
  # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
  print(grades)
  picked.append(grades[0][1])
  
for i in picked:
  print(i)
