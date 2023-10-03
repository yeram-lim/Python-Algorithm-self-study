def solution(maps):
    answer = -1

    def visit(x, y, count):
        # print('🍎',x,y,count)
        if maps[x][y] == 1:
            count += 1
            maps[x][y] = -1 
            if x == len(maps) - 1 and y == len(maps) - 1:
                if answer > 0 and count < answer:
                    return count
                else:
                    return -1
            if x + 1 < len(maps):
                visit(x + 1, y, count)
            if x - 1 >= 0:
                visit(x - 1, y, count)
            if y + 1 < len(maps):
                visit(x, y + 1, count)
            if y - 1 >= 0:
                visit(x, y - 1, count)
            
    answer = visit(0, 0, 0)
    print(answer)
        
    return answer if answer else -1
  
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])