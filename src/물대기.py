# https://www.acmicpc.net/problem/1368

import sys

input = sys.stdin.readline

def find(x):
  if x != parents[x]:
    parents[x] = find(parents[x])
  
  return parents[x]

def union(x, y):
  x_root = find(x)
  y_root = find(y)
  
  if x_root == y_root:
    return False
  
  if rank[x_root] > rank[y_root]:
    parents[y_root] = x_root
  elif rank[y_root] > rank[x_root]:
    parents[x_root] = y_root
  else:
    parents[x_root] = y_root
    rank[y_root] += 1
  
  return True
 
N = int(input())

parents = list(range(N + 1))
rank = [0] * (N + 1)
count = 0
result = 0

self_weight = [int(input()) for _ in range(N)]
matrix = [list(map(int, input().split())) for _ in range(N)]
connect_weight = []

for i in range(N):
  for j in range(i + 1, N):
    connect_weight.append((i, j, matrix[i][j]))

for index, w in enumerate(self_weight):
  connect_weight.append((N, index, w))
  
connect_weight.sort(key=lambda element: element[2])

for x, y, w in connect_weight:
  if union(x, y):
    result += w
    count += 1
    
  if count == N:
    break
  
print(result)
