# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

tomatoes = [(i, j, 0) for i in range(N) for j in range(M) if board[i][j] == 1]
queue = deque(tomatoes)

while queue:
  current_row, current_column, time = queue.popleft()
  
  for r, c in zip(dr, dc):
    next_row = current_row + r
    next_column = current_column + c
    
    if not (0 <= next_row < N and 0 <= next_column < M):
      continue
    
    if board[next_row][next_column] != 0:
      continue
    
    board[next_row][next_column] = 1
    queue.append((next_row, next_column, time + 1))

if [element for sublist in board for element in sublist if element == 0]:
  print(-1)
else:
  print(time)
