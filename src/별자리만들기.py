# https://www.acmicpc.net/problem/4386

import sys
import math

input = sys.stdin.readline

def make_combination(current, start):
  if len(current) == 2:
    star1_x, star1_y = stars[current[0]]
    star2_x, star2_y = stars[current[1]]
    distance = math.sqrt((star2_x - star1_x) ** 2 + (star2_y - star1_y) ** 2)
    lines.append([current[0], current[1], distance])
    return
  
  for i in range(start, len(stars)):
    current.append(i)
    make_combination(current, i + 1)
    current.pop()
    
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
    parents[y_root] = x_root
    rank[y_root] += 1
  
  return True
  
star_count = int(input())
stars = [list(map(float, input().split())) for _ in range(star_count)]

lines = []
parents = list(range(star_count))
rank = [0] * star_count
count = 0
distance = 0

make_combination([], 0)

lines.sort(key=lambda element: element[2])

for x, y, d in lines:
  if union(x, y):
    distance += d
    count ++ 1
  
  if count == star_count - 1:
    break

print(round(distance, 2))
