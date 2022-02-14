# not yet

n = int(input())

result = ""
done = []
rdict = dict()
for i in range(n):
    do, action, sec = input().split()
    sec = int(sec)
    rdict[sec] = [do, action]
print(rdict)

for key in rdict.keys():
    if rdict[key][0] == "type":
        result+= rdict[key][1]
        done.append(result)
    else:
        time = (key) - int(rdict[key][1])
        for j in range(key, time-1):
            if int(j) in rdict:
                if rdict[int(j)] == "type":
                    result = 0
