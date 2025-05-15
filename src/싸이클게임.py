# https://www.acmicpc.net/problem/20040
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
    return True
  
  if rank[x_root] > rank[y_root]:
    parents[y_root] = x_root
  elif rank[y_root] > rank[x_root]:
    parents[x_root] = y_root  
  else:
    parents[x_root] = y_root
    rank[y_root] += 1    
  
  return False

n, m = map(int, input().split())
parents = list(range(n))
rank = [0] * n
answer = 0

for i in range(m):
  x, y = map(int, input().split())
  if union(x, y):
    answer = i + 1
    break  

print(answer)
