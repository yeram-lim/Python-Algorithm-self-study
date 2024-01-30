from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    x = [-1, 0, 1, 0]
    y = [0, -1, 0, 1]
    
    moving_available_x_list = []
    moving_available_y_list = []
    
    for rect in rectangle:
      moving_available_x_list.append((rect[0], rect[2]))
      moving_available_y_list.append((rect[1], rect[3]))
    
    q = deque()
    for j in range(len(rectangle) - 1):
      moving_available_x = moving_available_x_list[j]
      moving_available_y = moving_available_y_list[j]
      if characterX <= moving_available_x[1] and characterX >= moving_available_x[0] and characterY <= moving_available_y[1] and characterY >= moving_available_y[0]:
        q.append((characterX, characterY, 0, j))
        
    # print(q)
    c = 0
    while q and c < 5:
      print('🍎',q)
      character_x, character_y, step, rect_index = q.pop()
      
      if character_x == itemX and character_y == itemY:
        answer = step
        break
      
      for i in range(4):
        dx = character_x + x[i]
        dy = character_y + y[i]
        print('다음 좌표',dx, dy)
        
        included_rect_list = []
        for j in range(len(rectangle) - 1):
          moving_available_x = moving_available_x_list[j]
          moving_available_y = moving_available_y_list[j]
          if (dx == moving_available_x[0] and (dy <= moving_available_y[1] and dy >= moving_available_y[0])) or (dx == moving_available_x[1] and (dy <= moving_available_y[1] and dy >= moving_available_y[0])) or (dy == moving_available_y[0] and (dx <= moving_available_x[1] and dx >= moving_available_x[0])) or (dy == moving_available_y[1] and (dx <= moving_available_x[1] and dx >= moving_available_x[0])):
            included_rect_list.append(j)
            
        if (len(included_rect_list) == 1):
          q.append((dx, dy, step + 1, included_rect_list[0]))
      print('마지막', q)
      c +=1
    
    return answer
  
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))