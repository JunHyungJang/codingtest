n = int(input())

# dict 만들기
friend = []
frdic = dict()
for i in range(n):
    k = list((input()))
    flist = []
    for j in range(len(k)):
        if k[j] == 'Y':
            flist.append(j)
    frdic[i] = flist
       
result = []

# dict에서 근처 append, 근처의 근처 append, set으로 중복제거
for key in frdic.keys():
    frset = set()
    frset.update(frdic[key])
    for j in frdic[key]:
        frset.update(frdic[j])
    # print(frset)
    if key in frset:
        frset.remove(key)

    result.append(len(frset))

# print(frdic)
print(max(result))
# print(result)