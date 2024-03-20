n = int(input())

for _ in range(1):
    money = 1000 - n
    a,b,c,d,e,f = 0,0,0,0,0,0
    a = money // 500
    b = (money % 500) // 100
    c = (money % 100) // 50
    d = (money % 50) // 10
    e = (money % 10) // 5
    f = (money % 5) // 1

    print(sum([a,b,c,d,e,f]))