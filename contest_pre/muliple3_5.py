N = int(raw_input())
k = 0
while k < N:
    count3 = 0
    count5 = 0
    sum = 0
    j = 0
        a = int(raw_input())
    while j < a :
        if j%3 == 0:
            count3 = count3 + j
        elif j%5 == 0:
            count5 = count5 + j

        sum = count3 + count5
        j = j + 1

        if j == a:
            break
    print(sum)

        if k == N:
            break