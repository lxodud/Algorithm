# https://www.acmicpc.net/problem/10971
import sys

input = sys.stdin.readline

def make_permutation(city, depth, cost):
  global min_cost
  if cost >= min_cost:
    return
  
  if depth == n-1 and w[city][0] > 0:
    min_cost = min(min_cost, cost + w[city][0])

  for next_city in range(n):
    if not visited[next_city] and w[city][next_city] > 0:
      visited[next_city] = True
      make_permutation(next_city, depth + 1, cost + w[city][next_city])
      visited[next_city] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_cost = 1000000 * 10

visited[0] = True
make_permutation(0, 0, 0)

print(min_cost)
