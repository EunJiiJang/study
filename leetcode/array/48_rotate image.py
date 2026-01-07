from typing import List

matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))

# matrix[:] 는 값만 바꾼다는 의미
# *matrix는 내부의 모든 리스트를 풀어서 파라미터로 전달
# ::-1은 역정렬 789가 인덱스 0번에
# zip은 같은 index 끼리 묶는거 그대신 리스트요소가 아닌 튜플이됨 ->(1,2,3)
# map은 괄호안에 첫번째인자의 형태로 변화시킴