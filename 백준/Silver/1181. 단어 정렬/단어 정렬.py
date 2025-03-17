import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

unique_words = sorted(set(words), key=lambda x: (len(x), x))

for w in unique_words:
  print(w)