case = int(input())
for i in range(case):
    limit = 60
    line = input().split()
    if line[1] == "true":
        limit +=5

    if int(line[0]) <= limit:
        print("no ticket")
    elif int(line[0]) <= limit + 20:
        print("small ticket")
    else:
        print("big ticket")
