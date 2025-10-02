case = int(input())
for i in range(case):
    scores = input().split()
    scores.sort()
    print(scores[-1])
