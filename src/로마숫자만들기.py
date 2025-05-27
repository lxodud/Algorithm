# https://www.acmicpc.net/problem/16922

import sys

def make_combinations_with_replacement(current, start):
  if len(current) == length:
    result.append(sum(current[:]))
    return
  
  for i in range(start, len(numbers)):
    current.append(numbers[i])
    make_combinations_with_replacement(current, i)
    current.pop()

input = sys.stdin.readline

length = int(input())
numbers = [1, 5, 10, 50]
result = {}

print(len(set(map(sum, combinations_with_replacement(numbers, length)))))
