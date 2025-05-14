# https://www.acmicpc.net/problem/11286

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
  number = int(input())
  
  if number == 0:
    if heap:
      print(heappop(heap)[1])
    else:
      print(0)
  else:
    heappush(heap, [abs(number), number])
