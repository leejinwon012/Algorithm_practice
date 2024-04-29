def solution(arr):
    while (True):
        if len(arr) & len(arr)-1 == 0:
            return arr
        else:
            arr.append(0)