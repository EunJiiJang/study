def is_available(cadidate,current_col):
    current_row = len(cadidate)
    for queen_row in range(current_row):
        if cadidate[queen_row] == current_col or abs(cadidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(N,current_row,current_cadidate,final_result):
    if current_row == N:
        final_result.append(current_cadidate[:])
        return
    for candidate_col in range(N):
        if is_available(current_cadidate,candidate_col):
            current_cadidate.append(candidate_col)
            DFS(N,current_row+1,current_cadidate,final_result)
            current_cadidate.pop()




def solve_n_queens(N):
    final_result = []
    DFS(N,0,[],final_result)
    return final_result

print(solve_n_queens(4))
