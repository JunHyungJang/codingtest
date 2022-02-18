import sys

input = sys.stdin.readline



def finding(phone,m):
    for i in range(m-1):
        # print(phone[i], phone[i+1][:len(phone[i])])
        if phone[i] in phone[i+1][:len(phone[i])]:
            
            return 'NO'
        else:
            pass
    
    return "YES"
n = int(input())

for i in range(n):
    phone = []
    m = int(input())
    for j in range(m):
        k = input().rstrip()
        # print(k)
        phone.append(k)
    phone.sort()
    # print(phone)
    
    print(finding(phone,m))
            
                
    
