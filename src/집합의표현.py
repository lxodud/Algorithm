# https://www.acmicpc.net/problem/1717

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x]) # path compression

  return parent[x]

def union(x, y):
  x_root = find(x)
  y_root = find(y)
  
  if x_root == y_root:
    return
  
  if rank[x_root] > rank[y_root]:
    parent[y_root] = x_root
  elif rank[y_root] > rank[x_root]:
    parent[x_root] = y_root
  else:
    parent[x_root] = y_root
    rank[y_root] += 1
    
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[y_root] > rank[x_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1

n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

for _ in range(m):
  command, a, b = map(int, input().split())
  
  if command == 0:
    union(a, b)
  else:
    if find(a) == find(b):
      print("YES")
    else:
      print("NO")
      
