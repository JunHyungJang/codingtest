import sys
from collections import deque

input = sys.stdin.readline

while 1:
    a = deque(list(map(int,(input().rstrip()))))
    if len(a) == 1 and a[0] == 0:
        break
    while 1:
        # print(a)
        if len(a) == 1 or len(a) == 0:
            print('yes')
            break
        else:
            left = a.popleft()
            right = a.pop()
            if left == right :
                pass
            else:
                print('no')
                break
        
    