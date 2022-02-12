from itertools import combinations
import math
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    result = math.factorial(b)/ (math.factorial(a) * math.factorial(b-a))
    print(int(result))
