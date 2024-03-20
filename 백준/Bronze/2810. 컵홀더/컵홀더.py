N = int(input()) # 좌석 수
seat = input() # 좌석 정보를 입력받음

couple = seat.count('LL') # 커플석의 개수

if couple <= 1:
    print(N)
else:
    print(N-couple + 1)
