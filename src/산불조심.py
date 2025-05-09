# https://dailyalgo.kr/ko/problems/65

from collections import deque

def solution(mountain):
  dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
  initail_fires = [(i, j, 0) for i in range(len(mountain)) for j in range(len(mountain)) if mountain[i][j] == 2]
  
  queue = deque(initail_fires)
    
  while queue:
    current_row, current_column, t = queue.popleft()
      
    for r, c in zip(dr, dc):
      next_row = current_row + r
      next_column = current_column + c
        
      if not (0 <= next_row < len(mountain) and 0 <= next_column < len(mountain)):
        continue
        
      if mountain[next_row][next_column] != 0:
        continue
      
      mountain[next_row][next_column] = 2
      queue.append((next_row, next_column, t + 1))
      
  return t
