import itertools

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
num = list(itertools.permutations(data, 3))

n = int(input())
cnt = 0
for _ in range(n):
    n, s, b = map(int, input().split()) 
    n = list(str(n))
    cnt = 0
    for i in range(len(num)): 
        strike = ball = 0 
        i -= cnt # num[0]부터 조회해야함 
        for j in range(3): 
            if num[i][j] == n[j]: # 입력한 숫자(한자리)와 num의 숫자(한자리)가 같으면 strike ++ 
                strike += 1 
            elif n[j] in num[i]: # 입력한 숫자(한자리)가 num안에 들어있으면 ball ++ 
                ball += 1 
        if (strike != s) or (ball != b): # 입력받은 s,b와 다르면 num에서 삭제 
            num.remove(num[i]) 
            cnt += 1 
                    
print(len(num))


