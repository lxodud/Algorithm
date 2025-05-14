# https://www.acmicpc.net/problem/20364

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
occupied_lands = [False] * (N + 1)

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
