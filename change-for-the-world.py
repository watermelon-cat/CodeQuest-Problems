#easy question
testcases = int(input())
for i in range(testcases):
    Q = 0
    D = 0
    N = 0
    P = 0
    bill = []
    money = input()
    for i in money:
        bill.append(i)
    bill.remove("$")
    bill = "".join(bill)
    bill = float(bill)
    Q = round(bill, 2) // 0.25
    bill = bill%0.25
    D = round(bill, 2) // 0.10
    bill = bill%0.10
    N = round(bill, 2) // 0.05
    bill = bill%0.05
    P = round(bill, 2)//0.01
    bill = bill%0.01
    print("Quarters=",int(Q))
    print("Dimes=",int(D))
    print("Nickles=",int(N))
    print("Pennies=",int(P))
