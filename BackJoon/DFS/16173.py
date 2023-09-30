n = int(input())
board = []

for i in range(n):
  a = input()
  board.append(list(map(int, a.split())))
  
x, y = 0, 0
visited = []
arrived = False

def visit(_x, _y):
  global arrived
  if (_y, _x) in visited or arrived:
    return
  
  visited.append((_y, _x))
  step = board[_y][_x]
  
  if _x < n and _x + step < n:
    if board[_y][ _x + step] == -1:
      arrived = True
      return
    visit(_x + step, _y)
    
  if _y < n and _y + step < n:
    if board[_y + step][ _x] == -1:
      arrived = True
      return
    visit(_x, _y + step)
    
visit(x, y)
if arrived:
  print('HaruHaru')
else:
  print('Hing')