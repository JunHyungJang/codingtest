from collections import deque

k = list((input()))
q = deque(k)


t = []
flag = 1


def finding():
    if len(q) == 0:
        return 1
    x = q.popleft()

    if x == "(":
        return 2 * finding() + finding()
    elif x == "[":
        return 3 * finding() + finding()
    elif x == ")":
        return 1 
    elif x == "]":
        return 1 

print(finding())


