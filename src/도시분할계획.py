# https://www.acmicpc.net/problem/1647

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
    
N, M = map(int, input().split())
parents = list(range(N + 1))
rank = [0] * (N + 1)

queries = [list(map(int, input().split())) for _ in range(M)]
queries.sort(key=lambda element: element[2])

weight = 0
count = 0

for A, B, C in queries:
  if N == 2:
    break
  
  if union(A, B):
    weight += C
    count += 1
  
  if count == N - 2:
    break

print(weight)
