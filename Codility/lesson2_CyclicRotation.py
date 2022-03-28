
def solution(A, K):
    N=len(A)
    if N <2:
        return A
    if K>=N:
        K = K%N
    return A[N-K:]+A[:N-K]


A = [3, 8, 9, 7, 6]
K = 3
solution(A, K)