testcases = int(input("testcases:"))
for i in range(testcases):
    eq = input("What's your equation?").split()
    num1 = float(eq[0])
    num2 = float(eq[2])
    op = eq[1]
    if op == "+":
        result1 = num1 + num2
        result2 = num2 + num1
    elif op == "-":
        result1 = num1 - num2
        result2 = num2 - num1
    elif op == "*":
        result1 = num1 * num2
        result2 = num2 * num1
    elif op == "/":
        result1 = num1 / num2
        result2 = num2 / num1
        result1 = round(result1 + .001, 1)
        result2 = round(result2 + .001, 1)
    print(f"{result1} {result2}\n")
    
