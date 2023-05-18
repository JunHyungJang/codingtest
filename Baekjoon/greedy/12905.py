from collections import deque

w = list(input())
word = list(input())
q = deque()
q.append(w)
def finding():
    while word:
        if word[-1] == 'A':
            word.pop()
        elif word[-1] == 'B':
            word.pop()
            word.reverse()
        if word == w:
            return 1
    return 0

print(finding())
