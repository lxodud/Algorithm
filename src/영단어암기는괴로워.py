# https://www.acmicpc.net/problem/20920

import sys

from collections import Counter

def sortCondition(element):
  return wordsDic[element], len(element)

input = sys.stdin.readline

N, M = list(map(int, input().split()))

words = list(filter(lambda word: len(word) >= M,[input().rstrip() for _ in range(N)]))
wordsDic = Counter(words)

words = sorted(list(set(words)))
words = sorted(words, key=sortCondition, reverse=True)

print(*words, sep="\n")
