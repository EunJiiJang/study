n = int(input())

cir = []
st = []
for i in range(n):
    x , r = map(int,input().split())
    cir.append([x-r,i,0])
    cir.append([x+r,i,1])
cir.sort()

for i in range(n):
    fir =  cir[i][2]
    if fir == 0:
        st.append(cir[i])
    else:
        if st[-1][2] == 0:
            if st[-1][1] == cir[i][1]:
                st.pop()
            else:
                print("NO")
                exit(0)

print("YES")
