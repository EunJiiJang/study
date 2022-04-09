def solution(path):
    answer = []
    path_list = list(path)
    cnt = 1
    for i in range(1,len(path_list)):
        result = ""
        if path_list[i] == path_list[i-1]:
            cnt += 1
        else:
            cnt = 1
            if path_list[i] == 'S':
                result = "Time "+str(i-cnt)+": Go straight "+str(cnt*100)+"m and turn right"
            elif path_list[i] == 'N':
                result = "Time "+str(i-cnt)+": Go straight "+str(cnt*100)+"m and turn left"
            answer.append(result)
    return answer





path = "EEESEEEEEENNNN"
답 = [
"Time 0: Go straight 300m and turn right",
"Time 3: Go straight 100m and turn left",
"Time 5: Go straight 500m and turn left"]


print(solution(path))