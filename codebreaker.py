#solved
import string
testcases = int(input())
for i in range(testcases):
    table = {
        "A" : 0, 
        "B" : 0,
        "C" : 0, 
        "D" : 0,
        "E" : 0, 
        "F" : 0,
        "G" : 0, 
        "H" : 0,
        "I" : 0,
        "J" : 0, 
        "K" : 0,
        "L" : 0, 
        "M" : 0,
        "N" : 0, 
        "O" : 0,
        "P" : 0, 
        "Q" : 0,
        "R" : 0, 
        "S" : 0,
        "T" : 0, 
        "U" : 0,
        "V" : 0, 
        "W" : 0,
        "X" : 0, 
        "Y" : 0,
        "Z" : 0, 
    }
    sentances = int(input())
    list = []
    sentancelength = 0
    for i in range(sentances):
        list.append(input().lower())

    for i in list:
        for k in i:
            if k.upper() in table.keys():
                sentancelength += 1
                table[k.upper()] += 1
        
    for key,value in table.items():
        table[key] = value/sentancelength * 100

    
    for key,value in table.items():
        print(f"{key}: {value:.2f}%")
