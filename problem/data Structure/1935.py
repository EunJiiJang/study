n = int(input())
x = input()
num = [0]*n
for i in range(n):
    num[i] = int(input())
st = []

for i in x:
    if 'A' <= i <= 'Z':
        st.append(num[ord(i)-ord('A')])
    else:
        b = st.pop()
        a = st.pop()
        if i == '+':
            st.append(a+b)
        if i == '-':
            st.append(a-b)
        if i == '*':
            st.append(a*b)
        if i == '/':
            st.append(a/b)
print('%.2f' %st[0])
        