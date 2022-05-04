import re
def solution(new_id):
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    answer = re.sub('\.\.+','.',answer)
    answer = answer.strip('.')
    if answer == '': answer+='a'
    answer = answer[:15].rstrip('.')
    answer += answer[-1]*(3-len(answer))

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))