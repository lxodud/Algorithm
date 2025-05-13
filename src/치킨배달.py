# https://www.acmicpc.net/problem/15686

import sys
from collections import deque

input = sys.stdin.readline

def make_min_length(best_chickens):
  current_city_distance = 0
  
  for house_row, house_column in houses:
    min_distance = float('inf')
    
    for chicken_row, chicken_column in best_chickens:
      min_distance = min(min_distance, abs(house_row - chicken_row) + abs(house_column - chicken_column))
    
    current_city_distance += min_distance
    
    if current_city_distance >= min_city_distance:
      return min_city_distance
  
  return current_city_distance

def make_combination(start, current):
  if len(current) == M:
    global min_city_distance
    min_city_distance = min(min_city_distance, make_min_length(current))
    return
  
  for i in range(start, len(chickens)):
    current.append(chickens[i])
    make_combination(i + 1, current)
    current.pop()

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

min_city_distance = float('inf')

for i in range(N):
  for j in range(N):
    if board[i][j] == 1:
      houses.append((i, j))
    elif board[i][j] == 2:
      chickens.append((i, j))

make_combination(0, [])  

print(min_city_distance)
