# https://www.acmicpc.net/problem/1100

import sys

input = sys.stdin.readline

matrix = [list(input().rstrip()) for _ in range(8)]
result = 0

for i in range(8):
  for j in range(8):
    if matrix[i][j] == "F" and (i + j) % 2 == 0:
      result += 1
      
print(result)
