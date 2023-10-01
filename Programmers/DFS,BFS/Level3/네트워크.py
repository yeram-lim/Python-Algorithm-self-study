# 다음에 다시 풀기!
# def solution(n, computers):
#     answer = 0
#     answers = []
    
#     def detect(x, y):
#         print('🍎 xy는?',x,y)
#         if x != y:
#             if computers[x][y]:
#                 is_inserted = False
#                 print('🍊 answers',answers)
#                 for list in answers:
#                     # x, y가 리스트 안에 둘 다 있는 경우
#                     if x in list and y in list:
#                         is_inserted = True
#                         break
                        
#                     # x, y가 리스트 안에 하나만 있는 경우
#                     if not (x in list and y in list) or x in list or y in list:
#                         if list[0] == x:
#                             list.insert(0, y)
#                             is_inserted = True
#                             break
#                         if list[0] == y:
#                             list.insert(0, x)
#                             is_inserted = True
#                             break
#                         if list[-1] == x:
#                             list.append(y)
#                             is_inserted = True
#                             break
#                         if list[-1] == y:
#                             list.append(x)
#                             is_inserted = True
#                             break
                
#                 if not is_inserted:
#                     if x > y:   
#                         answers.append([x, y])
#                     else:
#                         answers.append([y, x])
            
#         if x + 1 < n:
#           detect(x + 1, y)
#         if y + 1 < n:
#           detect(x, y + 1)
    
#     detect(0, 0)
    
#     count = 0
#     for list in answers:
#       count += len(list)
    
#     return len(answers) + (n - count)
  
# 남의 풀이
def solution(n, computers):
  answer = 0
  visited = [False] * n
  
  def visit(node_index):
    visited[node_index] = True
    
    for i in range(n):
      if not visited[i] and computers[node_index][i]:
        visit(i)
  
  for node_index in range(n):
    if not visited[node_index]:
      visit(node_index)
      answer += 1
  return answer
    
a = solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])
print('a', a)