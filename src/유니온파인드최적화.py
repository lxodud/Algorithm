# https://dailyalgo.kr/ko/problems/91

def solution(n, queries):
  def find(x):
    if x != parents[x]:
      parents[x] = find(parents[x])
    
    return parents[x]
  
  def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if x_root == y_root:
      return
    
    if rank[x_root] > rank[y_root]:
      parents[y_root] = x_root
    elif rank[y_root] > rank[x_root]:
      parents[x_root] = y_root
    else:
      parents[x_root] = y_root
      rank[y_root] += 1
      
  parents = list(range(n + 1))
  rank = [0] * (n + 1)
  answer = []
    
  for command, x, y in queries:
    if command == -1:
      union(x, y)
    else:
      answer.append(find(x) == find(y))
  
  return answer
