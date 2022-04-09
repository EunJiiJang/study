def solution(call):
    call =call
    answer = ''
    s = call.lower()
    tmp =''
    lst = {}
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i:j+1]==s[j+1:(j+1)+(j-i)+1]:
                new_tmp=s[i:j+1]
                if new_tmp != '':
                    lst[new_tmp] = s.count(new_tmp)
    call_list = list(call)
    for i in call_list:
        if s.count(i)>0:
            lst[i] = s.count(i)
    max_num = max(lst.values())
    for i in lst:
        key,value = i,lst[i]
        if value == max_num:
            U = key.upper()
            L = key.lower()
            answer = str(call).replace(U, "")
            answer = str(answer).replace(L, "")


    return answer

call1 = "abcabcdefabc"
call2 = "ABCabcA"
call3 = "abcabca"
call4 = "abxdeydeabz"
print(solution(call4))
