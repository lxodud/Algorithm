# https://www.acmicpc.net/problem/1976

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
    return
  
  if rank[x_root] > rank[y_root]:
    parents[y_root] = x_root
  elif rank[y_root] > rank[x_root]:
    parents[x_root] = y_root
  else:
    parents[x_root] = y_root
    rank[y_root] += 1
      
# 도시의 수
N = int(input())
# 여행 계획에 속한 도시들의 수
M = int(input())

parents = list(range(N + 1))
rank = [0] * (N + 1)

for i in range(1, N + 1):
  pathes = list(map(int, input().split()))
  for j in range(i - 1, len(pathes)):
    if pathes[j] != 1:
      continue
    union(i, j + 1)
    
travle_plan = list(map(int, input().split()))
can_travle = True
root = find(travle_plan[0])

for plan in travle_plan[1:]:  
  if root != find(plan):
    can_travle = False
    break

if can_travle:
  print("YES")
else:
  print("NO")

