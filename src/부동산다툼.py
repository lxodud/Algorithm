# https://www.acmicpc.net/problem/20364

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

tree = [[-1, -1] for _ in range(N + 1)]
occupied_lands = [False] * (N + 1)

for node in range(1, N + 1):
  if node * 2 <= N:
    tree[node][0] = node * 2
  
  if node * 2 + 1 <= N:
    tree[node][1] = node * 2 + 1

for _ in range(Q):
  target = int(input())
  current_node = target
  face_occupied_land = -1
  
  while current_node != 1:
    if occupied_lands[current_node]:
      face_occupied_land = current_node
      
    current_node //= 2
    
  if face_occupied_land == -1:
    print(0)
    occupied_lands[target] = True
  else:
    print(face_occupied_land)
