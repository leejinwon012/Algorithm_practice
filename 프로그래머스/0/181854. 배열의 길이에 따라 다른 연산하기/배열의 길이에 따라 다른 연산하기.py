def solution(arr, n):
    for index, i in enumerate(arr):
        if len(arr) % 2 != 0:
            if index % 2 == 0:
                arr[index] += n
        else:
            if index % 2 != 0:
                arr[index] += n
    return arr