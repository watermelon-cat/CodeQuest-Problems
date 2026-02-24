def br(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

testcases = int(input())
for i in range(testcases):
    eq = input().split()
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
    print(f"{br(result1, 1)} {br(result2,1)}")
    
