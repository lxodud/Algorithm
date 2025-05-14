# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heappush, heappop, heapify

def solution(scoville, K):
  heapify(scoville)
  count = 0
  while True:    
    first = heappop(scoville) 
    if first >= K:
      break
    
    if len(scoville) == 0:
      return -1
    
    second = heappop(scoville)
    
    heappush(scoville, first + second * 2)
    count += 1
  
  return count
