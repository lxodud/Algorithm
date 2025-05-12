# https://dailyalgo.kr/ko/problems/97
def solution(n):
  def make_permutations(depth, previous):
    if depth - 1 == previous:
      return
    
    if depth == n:
      nonlocal count
      count += 1
      return
    
    for i in range(0, n):
      if visited[i]:
        continue
      visited[i] = True
      make_permutations(depth + 1, i)
      visited[i] = False
    
  visited = [False] * n
  count = 0
  make_permutations(0, -2)
  
  return count
