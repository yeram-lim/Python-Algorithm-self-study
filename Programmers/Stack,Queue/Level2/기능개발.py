from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    
    while q:
        for i in range(len(q)):
            q[i] = q[i] + speeds[i]
            
        count = 0
        while len(q) > 0 and q[0] >= 100:
            q.popleft()
            count += 1
        if count > 0:
            answer.append(count)
    
    return answer
  
print(solution([93, 30, 55, 99],[1, 30, 5, 2]))