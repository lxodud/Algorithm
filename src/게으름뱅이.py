# https://dailyalgo.kr/ko/problems/93

from heapq import heappush, heappop

def solution(todoList):
  priorities = {
    "CRITICAL": 0,
    "HIGH": 1,
    "MODERATE":2,
    "LOW": 3,
    "MINIMAL": 4
  }
  
  heap = []
  answer = []
  current_day = 1

  while current_day <= len(todoList) * 2:
    if current_day <= len(todoList):
      month, day, year  = todoList[current_day - 1][1].split("/")
      heappush(heap, [year, month, day, priorities[todoList[current_day - 1][2]], todoList[current_day - 1][0]])
    
    if current_day % 2 == 0:
      answer.append(heappop(heap)[4])
      
    current_day += 1
    
  return answer
