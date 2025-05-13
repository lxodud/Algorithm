# https://www.acmicpc.net/problem/12869

import sys
from collections import deque

input = sys.stdin.readline

count = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
  scv.append(0)
demages = [[9, 1, 3], [9, 3, 1], [3, 1, 9], [3, 9, 1], [1, 3, 9], [1, 9, 3]]
visited = [[[0 for _ in range(64)] for _ in range(64)] for _ in range(64)]

queue = deque()
visited[scv[0]][scv[1]][scv[2]] = 1
queue.append((scv)) 

while queue:
  a, b, c = queue.popleft()
  if visited[0][0][0] != 0:
    break
  
  for demage in demages:
    na = max(0, a - demage[0])
    nb = max(0, b - demage[1])
    nc = max(0, c - demage[2])
    
    if visited[na][nb][nc] != 0:
      continue
    
    visited[na][nb][nc] = visited[a][b][c] + 1;
    queue.append((na, nb, nc))

print(visited[0][0][0] - 1)
