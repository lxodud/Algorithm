# https://dailyalgo.kr/ko/problems/112

def solution(board):
  def make_permitation(depth, cost):  
    if depth == n:
      nonlocal max_sum
      max_sum = max(max_sum, cost)
    
    for i in range(0, n):
      if visited[i]:
        continue
      
      visited[i] = True
      make_permitation(depth + 1, cost + board[depth][i])
      visited[i] = False
  
  n = len(board)
  visited = [False] * n
  max_sum = 0
  make_permitation(0, 0)
  return max_sum
