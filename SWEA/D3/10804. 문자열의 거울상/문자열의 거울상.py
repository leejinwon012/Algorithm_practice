n = int(input())

for i in range(1, n + 1):
    test_case = input()
    answer = ""
    for j in test_case:
        if j == "b":
            answer += "d"
        elif j == "d":
            answer += "b"
        elif j == "p":
            answer += "q"
        elif j == "q":
            answer += "p"
        else:
            answer += j

    print(f"#{i} {answer[::-1]}") 
