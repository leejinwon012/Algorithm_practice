# SW 2007번 문제
for i in range(1, int(input())+1):
    test = input()
    result = ""

    for j in test:
        result += j
        if result[:len(result)//2] == result[len(result)//2:]:      # 슬라이싱 이론 정확히!
             break
    print(f"#{i} {len(result) // 2}")

