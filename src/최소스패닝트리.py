# https://www.acmicpc.net/problem/1197

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

V, E = map(int, input().split())
queries = []
parents = list(range(V + 1))
rank = [0] * (V + 1)

for _ in range(E):
  queries.append(list(map(int, input().split())))

queries.sort(key=lambda element: element[2])

result = 0
count = 0
for A, B, C in queries:
  if union(A, B):
    result += C
    count += 1
  
  if count == E:
    break

print(result)
