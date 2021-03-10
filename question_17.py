# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

num1 = input("enter the first number")
num2 = input("enter the second number")
if num1.isdigit() and num2.isdigit():
    num2 = float(num2)
    num1 = float(num1)
    operator = input("enter the operator")
    if operator in '+-*/':
        if operator == '+':
            print("the sum is ", (num1 + num2))

        elif operator == '-':
            print("the result is ", (num1 - num2))

        elif operator == '*':
            print("the result is ", (num1 * num2))

        elif operator == "/":
            if num2 is 0:
                raise ZeroDivisionError
            else:
                result = num1 / num2
            print("the result is ", result)
    else:
        raise Exception("invalid operator")

else:
    raise Exception("invalid entry : enter numbers only")
