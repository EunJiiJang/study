import sys
input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int,input().split())
    lst = list(map(int,input().split()))
    lst_ = [0 for i in range(a)]
    lst_[b] =1
    cnt = 0
    while True:
        if lst[0] == max(lst):
            cnt += 1
            if lst_[0] == 1:
                print(cnt)
                break
            else:
                del lst[0]
                del lst_[0]

        else:
            lst.append(lst[0])
            del lst[0]
            lst_.append(lst_[0])
            del lst_[0]
