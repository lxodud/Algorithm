# https://www.acmicpc.net/problem/2468

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_row, start_column, height):
  queue = deque([(start_row, start_column)])
  
  while queue:
    current_row, current_column = queue.popleft()
    
    for r, c in zip(dr, dc):
      next_row = current_row + r
      next_column = current_column + c

      if not (0 <= next_row < N and 0 <= next_column < N):
        continue
      
      if visited[next_row][next_column]:
        continue
      
      if board[next_row][next_column] <= height:
        continue
      
      visited[next_row][next_column] = True
      queue.append((next_row, next_column))
      
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_day = max([element for sublist in board for element in sublist])
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
results = []
max_safe = 1

for height in range(1, max_day + 1):
  count = 0
  visited = [[False] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if visited[i][j] or board[i][j] <= height:
        continue
      
      count += 1
      visited[i][j] = True
      bfs(i, j, height)
  
  max_safe = max(max_safe, count)

print(max_safe)
