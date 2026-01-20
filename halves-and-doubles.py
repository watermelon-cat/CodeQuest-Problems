testcases = int(input())
for i in range(testcases):
    firstnum = []
    secnum = []
    line = input().split()
    firstnum.insert(0, int(line[0]))
    secnum.insert(0, int(line[1]))
    while int(firstnum[-1]) > 1:
        firstnum.append(int(firstnum[-1])/2)
        secnum.append(int(secnum[-1])*2)
    Sum = 0
    for i in range(len(firstnum)):
        if firstnum[i] % int(firstnum[i]) > 0:
            print((int(firstnum[i])), "*", end = " ", sep ="")
            
        else:
            print(firstnum[i], end = " ")
            

        if int(firstnum[i]) % 2 == 0:

            print(secnum[i], "***")
        else:
            print(secnum[i])
            Sum += secnum[i]
    print(Sum)
