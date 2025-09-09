num = int(input())
for i in range(num):
    line = input().split()  #split() turns anything seperated by a space into a string list
    print(int(line[0]) + int(line[1]), int(line[0]) * int(line[1]))  #put int() infront of the list so that it can add them together
