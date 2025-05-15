# https://dailyalgo.kr/ko/problems/89

def solution(n, syncs):
  def find(x):
    if x != parents[x]:
      parents[x] = find(parents[x])
  
    return parents[x]
  
  def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    if x_root == y_root:
      return False
    
    if rank[x_root] > rank[y_root]:
      parents[y_root] = x_root
    elif rank[y_root] > rank[x_root]:
      parents[x_root] = y_root
    else:
      parents[x_root] = y_root
      rank[y_root] += 1
    
    return True
    
  parents = list(range(n + 1))
  rank = [0] * (n + 1)

  syncs.sort(key=lambda element: element[2])
  result = 0
  count = 0
  
  for x, y, w in syncs:
    if union(x, y):
      result += w
      count += 1
      
    if count == n - 1:
      break

  if count == n - 1:
    return result
  else:
    return -1
