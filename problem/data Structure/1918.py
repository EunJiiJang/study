n =input()
st = []
res = ''
for i in n:
    if 'A' <= i <= 'Z':
        res += i
    else:
        if i =='(':
            st.append(i)
        elif i == '*' or i == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                res += st.pop()
            st.append(i)
        elif i == '+' or i == '-': 
            while st and st[-1] != '(': 
                res+= st.pop() 
            st.append(i) 
        elif i == ')':
            while st and st[-1] != '(': 
                res += st.pop() 
            st.pop() 
while st :
    res+=st.pop() 
print(res)
