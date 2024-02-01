from collections import deque


def solution(tickets):
    q = deque()
    START = 'ICN'
    answer = [START]
    
    q.append([False, START])
    while q:
      [current_start, current_end] = q.pop()
      ticket_list = []
      for index, ticket in enumerate(tickets):
        if ticket:
          [start, end] = ticket
          if start == current_end:
            ticket_list.append((index, ticket))
      
      if len(ticket_list) == 0:
        break
      if len(ticket_list) > 1:
        ticket_list.sort(key = lambda x : x[1][1])
      ticket_index, final_ticket = ticket_list[0][0], ticket_list[0][1]
      q.append(final_ticket)
      answer.append(final_ticket[1])
      tickets[ticket_index] = 0
      
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))