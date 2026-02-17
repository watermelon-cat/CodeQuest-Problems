#unfinished
#fix formating

def tree(list):
    if len(list) >= 3:
        root = list[len(list)//2]
        print("    " * (len(list)//2), end = "")
        print(root)
    else:
        print(list, "   ", end= "")
        return
    lesslist = []
    morelist = []
    for i in list:
        if i < root:
            lesslist.append(i)
        elif i > root:
            morelist.append(i)
    tree(lesslist)
    tree(morelist)


    

testcases = int(input())
for i in range(testcases):
    sortedlist = []
    numbers = input().split()
    for i in numbers:
        sortedlist.append(int(i))
    sortedlist.sort()
    print(sortedlist)
    tree(sortedlist)
