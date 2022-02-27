import sys

# from pyparsing import Word

input = sys.stdin.readline

n = int(input())

word = []
for i in range(n):
    k = input().rstrip()
    word.append(k)

word = set(word)
word = list(word)
word.sort()
word.sort(key = len)

# answer = set(word)
# print(word)
# print(answer)
for i in word:
    print(i)
