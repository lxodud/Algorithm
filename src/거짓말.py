# https://www.acmicpc.net/problem/1043

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
  
  if x_root in truth_numbers:
    parents[y_root] = x_root
  elif y_root in truth_numbers:
    parents[x_root] = y_root
  else:
    parents[x_root] = y_root
    
N, M = map(int, input().split())

truth = list(map(int, input().split()))
truth_numbers = set(truth[1:])
parents = list(range(N + 1))
parties = []

for _ in range(M):
  party = list(map(int, input().split()))
  participants = party[1:]
  parties.append(set(participants))
  
  for i in range(len(participants) - 1):
    union(participants[i], participants[i + 1])

dont_lie_numbers = []
for i in range(1, len(parents)):
  if find(i) in truth_numbers:
    dont_lie_numbers.append(i)

count = 0
for party in parties:
  can_lie = set(party).isdisjoint(dont_lie_numbers)
  
  if can_lie:
    count += 1

print(count)
