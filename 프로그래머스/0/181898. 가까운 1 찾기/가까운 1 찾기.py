def solution(arr, idx):
    for index, i in enumerate(arr):
        if index >= idx and i == 1:
            return index
    return -1