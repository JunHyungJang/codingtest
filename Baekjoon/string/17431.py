import sys

input = sys.stdin.readline

wordd = list(input().rstrip())
tag = False
word = ''
result = ''

for w in wordd:
    # print(result,word)
    if tag ==False:
        if w == '<':
            tag = True
            word = word+w
        elif w == " ":
            word = word + w
            result = result + word
            word = ""
        else:
            word= w + word
    
    else:
        word = word+w
        if w == ">":
            tag =False
            result = result + word
            word = ""
    # print(word)

print(result+word)