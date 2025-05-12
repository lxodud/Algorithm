# https://www.acmicpc.net/problem/1068

import sys

input = sys.stdin.readline

def order(node):
  if not tree[node]:
    global count
    count += 1
    return
  
  for next_node in tree[node]:
    order(next_node)

N = int(input())
tree = [[] for _ in range(N)]
parents = list(map(int, input().split()))
target_node = int(input())
count = 0

for child, parent in enumerate(parents):
  if parent == -1:
    root = child
    continue
  
  if child == target_node:
    continue
  
  tree[parent].append(child)

order(root)

if target_node == root:
  print(0)
else:
  print(count)
