# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

input = sys.stdin.readline
board_length = int(input())
board = [[0] * board_length for _ in range(board_length)]

apple_count = int(input())

for _ in range(apple_count):
  row, column = map(int, input().split())
  board[row - 1][column - 1] = 1
  
query_count = int(input())
queries = {}

for _ in range(query_count):    
  second, spin = input().split()
  queries[int(second)] = spin

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

snake = deque([(0, 0)])
direction = 0
game_time = 0

while True:
  game_time += 1
    
  nr = snake[-1][0] + dr[direction]
  nc = snake[-1][1] + dc[direction]
  
  if not (0 <= nr < board_length and 0 <= nc < board_length) or board[nr][nc] == 2:
    break
    
  snake.append((nr, nc))  
    
  if board[nr][nc] != 1:
    pn, pc = snake.popleft()  
    board[pn][pc] = 0 
    
  board[nr][nc] = 2
  spin = queries.get(game_time, "X")
  
  if spin == "D":
    direction = (direction + 1) % 4
  elif spin == "L":
    direction = (direction - 1) % 4

print(game_time)
