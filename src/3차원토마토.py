# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

for i in range(H):
  for j in range(N):
    for k in range(M):
      if board[i][j][k] == 1:
        queue.append((i, j, k, 0))
        
while queue:
  current_z, current_row, current_column, time = queue.popleft()
  
  for r, c, z in zip(dr, dc, dz):
    next_row = current_row + r
    next_column = current_column + c
    next_z = current_z + z
    
    if not (0 <= next_row < N and 0 <= next_column < M and 0 <= next_z < H):
      continue
    
    if board[next_z][next_row][next_column] != 0:
      continue
    
    board[next_z][next_row][next_column] = 1
    queue.append((next_z, next_row, next_column, time + 1))

def is_raw_tomato(box):
  for list in box:
    for sublist in list:
      if 0 in sublist:
        global time
        time = -1
        return

is_raw_tomato(board)
print(time)
