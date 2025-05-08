# https://www.acmicpc.net/problem/6603

import sys

input = sys.stdin.readline

def make_combination(current, start):
  if len(current) == 6:
    results.append(current[:])
    return
  
  for i in range(start, len(S)):
    current.append(S[i])
    make_combination(current, i + 1)
    current.pop()
  
while True:
  results = []
  test_case = list(map(int, input().split()))
  
  k = test_case[0]
  
  if k == 0:
    break
  
  S = test_case[1:]
  
  make_combination([], 0)
  for result in results:
    print(*result)

  print()
