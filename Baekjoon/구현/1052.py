n,k = map(int,input().split())
answer = 0
while bin(n).count('1') > k:
    plus = 2**(bin(n)[::-1].index('1'))
    answer+=plus
    n+= plus
print(answer)
# import sys
# from tkinter import BOTTOM
# input = sys.stdin.readline

# n,k = map(int,input().split())

# bottle = dict()
# bottle[1] = n
# print(sum(bottle.values()))

# total = 0

# liter= 1
# while sum(bottle.values()) != k:
#     # print(bottle)
#     # print(total)
#     print(total)
#     if bottle[liter] > 1:
#         if liter*2 in bottle:
#             bottle[liter*2] += bottle[liter] //2
#         else:
#             bottle[liter*2] = bottle[liter]//2
#         bottle[liter] = bottle[liter] % 2
#         liter = liter * 2
#     else:
#         liters = [liter for liter in bottle if bottle[liter] > 0]
#         # print(liters)
#         total+= liters[1] - liters[0]
#         bottle[liters[0]] += total
#         liter = liters[0]
# print(bottle)
# print(total)


# while 1:


# num, min = map(int,input().split())

# bottle = dict()
# bottle[1] = num
# # not finished

# liter = 1
# total = 0
# while liter in bottle:
#     if sum(list(bottle.values()))< min:
#         break
#     if bottle[liter]>1:
#         bottle[liter*2] = bottle[liter] //2
#         bottle[liter] = bottle[liter] % 2
#         liter = liter*2
#         print(bottle)
#     else:
#         liters = [liter for liter in bottle if bottle[liter]>0]
#         print(liters)
#         total+= liters[1]- liters[0]
#         bottle[liters[0]]+=total
#         print(bottle)


