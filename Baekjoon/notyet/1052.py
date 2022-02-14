num, min = map(int,input().split())

bottle = dict()
bottle[1] = num
# not finished

liter = 1
total = 0
while liter in bottle:
    if sum(list(bottle.values()))< min:
        break
    if bottle[liter]>1:
        bottle[liter*2] = bottle[liter] //2
        bottle[liter] = bottle[liter] % 2
        liter = liter*2
        print(bottle)
    else:
        liters = [liter for liter in bottle if bottle[liter]>0]
        print(liters)
        total+= liters[1]- liters[0]
        bottle[liters[0]]+=total
        print(bottle)

    
