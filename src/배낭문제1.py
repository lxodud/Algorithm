# https://dailyalgo.kr/ko/problems/61
def solution(volume, items):
  def make_combiantions(current_volume, price, start):
    if current_volume >= volume:
      return
    
    nonlocal max_price
    max_price = max(max_price, price)
    
    for i in range(start, len(items)):
      item_volume = items[i][0]
      item_price = items[i][1]
        
      make_combiantions(current_volume + item_volume, price + item_price, i + 1)

  max_price = 0
  make_combiantions(0, 0, 0)
  return max_price
