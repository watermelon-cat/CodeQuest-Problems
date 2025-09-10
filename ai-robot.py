direction = ["North"]

test = int(input())
xpos = 0
ypos = 0
line = input().split()
xpos = int(line[0])
ypos = int(line[1])

for i in range(test):
    for i in line[3]:
        if i == "R":
            if line[2] == "N":
                direction[0] = "east"
                line[2] = "E"
                continue
            elif line[2] == "E":
                direction[0] = "south"
                line[2] = "S"
                continue
            elif line[2] == "S":
                direction[0] = "west"
                line[2] = "W"
                continue
            elif line[2] == "W":
                direction[0] = "north"
                line[2] = "N"
                continue
        if i == "A":
            if direction[0] == "north":
                ypos +=1
                continue
            elif direction[0] == "east":
                xpos +=1
                continue
            elif direction[0] == "south":
                ypos -= 1
                continue
            elif direction[0] == "west":
                xpos -=1
                continue
        if i == "L":
            if line[2] == "N":
                direction[0] = "west"
                line[2] = "W"
                continue
            elif line[2] == "E":
                direction[0] = "north"
                line[2] = "N"
                continue
            elif line[2] == "S":
                direction[0] = "east"
                line[2] = "E"
                continue
            elif line[2] == "W":
                direction[0] = "south"
                line[2] = "S"
                continue
                

print(xpos, ypos, line[2])

    

