def solution(path):
    answer = []
    path_list = list(path)
    cnt = 1
    sec = 0
    for i in range(1,len(path_list)):
        result = ""
        if path_list[i] == path_list[i-1]:
            cnt += 1
        else:
            if cnt >= 5:
                sec += (6 - cnt)+1
                cnt = 5
            
            if path_list[i] == 'S' or path_list[i] == 'W':
                result = "Time "+str(sec)+": Go straight "+str(cnt*100)+"m and turn right"
            elif path_list[i] == 'N'or path_list[i] == 'E':
                result = "Time "+str(sec)+": Go straight "+str(cnt*100)+"m and turn left" 
            
            sec += cnt
            answer.append(result)
    return answer




path = "EEESEEEEEENNNN"
path2 = "SSSSSSWWWNNNNNN"

답 = [
"Time 0: Go straight 300m and turn right",
"Time 3: Go straight 100m and turn left",
"Time 5: Go straight 500m and turn left"]

print(solution(path2))