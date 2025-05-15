# https://dailyalgo.kr/ko/problems/90

def solution(n, queries):
  def find(x):
    while x != parents[x]:
      x = parents[x]
        
    return x
    
  def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if x_root == y_root:
      return

    if x_root < y_root:
      parents[y_root] = x_root
    else:
      parents[x_root] = y_root
  
  parents = list(range(n + 1))
  answer = []
  
  for command, x, y in queries:
    if command == -1:
      union(x, y)
    else:
      answer.append(find(x) == find(y))
  
  return answer
