#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    if len(sys.argv) > 2:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op == "+":
            print(calc.add(a, b))
        elif op == "-":
            print(calc.sub(a, b))
        elif op == "*":
            print(calc.mul(a, b))
        elif op == "/":
            print(calc.div(a,b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
