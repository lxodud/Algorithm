# https://www.acmicpc.net/status?user_id=xodud1998223&problem_id=7562&from_mine=1
import sys
from collections import deque

input = sys.stdin.readline

dr = [2, 2, -1, 1, -2, -2, -1, 1]
dc = [-1, 1, 2, 2, -1, 1, -2, -2]

test_case = int(input())

def bfs(start_row, start_column):
  queue = deque([(start_row, start_column)])
  
  while queue:
    current_row, current_column = queue.popleft()
    
    for r, c in zip(dr, dc):
      next_row = current_row + r
      next_column = current_column + c
      
      if not ( 0 <= next_row < length and 0 <= next_column < length):
        continue
      
      if board[next_row][next_column] != 0:
        continue
      
      board[next_row][next_column] = board[current_row][current_column] + 1
      queue.append((next_row, next_column))
  

for _ in range(test_case):
  length = int(input())
  start_row, start_column = map(int, input().split())
  target_row, target_column = map(int, input().split())
  
  board = [[0] * length for _ in range(length)]
  board[start_row][start_column] = 1 
  bfs(start_row, start_column)
  
  print(board[target_row][target_column] - 1)
