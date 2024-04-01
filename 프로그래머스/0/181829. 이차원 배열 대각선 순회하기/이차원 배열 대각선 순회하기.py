def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if 0 <= i + j <= k:
                answer += board[i][j]
    return answer