#unfinsished
#redo simple
counter = 0
line = input().split()

for i in range(len(line)):
    word = line[i] + line[-1]
    print(word)
print(word)
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        counter +=1

print(counter)
