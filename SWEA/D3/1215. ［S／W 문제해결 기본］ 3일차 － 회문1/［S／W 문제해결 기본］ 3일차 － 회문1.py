def count_palindromes(test, length):
    count = 0
    for i in range(8):
        for j in range(8 - length + 1):
            row = test[i][j:j + length]
            if row == row[::-1]:
                count += 1

            col = ""
            for k in range(length):
                col += test[j + k][i]
            if col == col[::-1]:
                count += 1
    return count

result = []
for _ in range(10):  # 테스트 케이스가 10번 반복됨
    length = int(input())
    test = []
    for _ in range(8):
        test.append(input())

    count = count_palindromes(test, length)
    result.append(count)

for i, count in enumerate(result, start=1):
    print("#{} {}".format(i, count))
