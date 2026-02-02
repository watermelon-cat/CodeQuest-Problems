testcases = int(input())
for i in range(testcases):
    numbers = input().split()
    sortedlist = []
    for j in range(len(numbers)):
        num = '0'
        for i in numbers:
            if i[0] > num:
                num = i
            if i[0] == num[0] and len(num) > 1 and num[0] < num[1]:
                pass
            elif i[0] == num[0] and len(i) < len(num):
                num = i
        sortedlist.append(num)
        numbers.remove(num)
    

    for i in sortedlist:
        print(i, end="")
    print()
