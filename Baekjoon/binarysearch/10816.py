import sys

input = sys.stdin.readline


def binary(start, end, k):
    mid = (start + end) //2

    if start > end:
        return 0

    if card[mid] == k:
        # print(card[mid], "card")
        # print(mid, "mid")
        answer = 1
        p = mid
        while 1 :
            p+= 1
            # print(p, "p")
            if 0<=p<=n-1:
                if card[p] == k:
                    answer+=1
            else:
                break
        p = mid
        while 1:
            p-=1
            
            if 0<=p<=n-1:
                if card[p] == k:
                    answer+=1
            else:
                break
        
        return answer
    
    elif card[mid] > k:
        end = mid-1
    
    else:
        start = mid+1

    return binary(start, end ,k)


n = int(input())

card = list(map(int,input().split()))
card.sort()

m = int(input())

clfy = list(map(int,input().split()))



start = 0
end = len(card)-1

for j in clfy:
    # print(start,end,j)
    print(binary(start,end,j), end =" ")

